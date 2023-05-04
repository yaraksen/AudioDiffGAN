import numpy as np
import torch
import torchaudio as T
import torchaudio.transforms as TT

from argparse import ArgumentParser
from concurrent.futures import ProcessPoolExecutor
from glob import glob
from tqdm import tqdm
import torchaudio
import torch.nn.functional as F
from pathlib import Path

from params import params
from os import path, mkdir


def transform(filename):
    audio, sr = T.load(filename)

    if sr != params.sample_rate:
        raise ValueError(
            f"Sample rate {sr} doesn't match target of {params.sample_rate}"
        )

    if audio.max() > 1 or audio.min() < -1:
        raise ValueError(
            f"Wrong audio format, samples should be between -1 and 1"
        )

    # audio = torch.clamp(audio[0], -1.0, 1.0)

    if audio.size(-1) < params.num_frames:
        audio = F.pad(audio, (0, params.num_frames - audio.size(-1)))
    
    if audio.size(-1) > params.num_frames:
        print('audio size is', audio.size(-1))
        audio = audio[..., :params.num_frames]
        print('new audio size is', audio.size(-1))

    mel_spec_transform = TT.MelSpectrogram(
        sample_rate=params.sample_rate,
        n_fft=params.n_fft,
        win_length=params.win_length,
        hop_length=params.hop_length,
        center=params.center,
        power=params.power,
        norm=params.norm,
        n_mels=params.n_mels,
        mel_scale=params.mel_scale)

    with torch.no_grad():
        # for i in range(3):
        #     audio = F.pad(audio, ((1024 - 160), (1024 - 160)), "reflect")
        # audio = F.pad(audio, (86, 86), "reflect")

        audio = F.pad(audio, ((1024 - 160) // 2, (1024 - 160) // 2), "reflect")

        spectrogram = mel_spec_transform(audio)
        spectrogram = torch.log(torch.clamp(spectrogram, min=1e-5))

        # padding audio to make mel shape (128, 128) 
        # doubling to make it sound more realistic
        spectrogram = torch.nn.functional.pad(spectrogram, (7, 7), "reflect")
        spectrogram = torch.nn.functional.pad(spectrogram, (7, 7), "reflect")

        np.save(f'{params.main_dir}/{params.mel_dir}/{filename.parent.name}/{filename.stem}.spec.npy', spectrogram.cpu().numpy())


def main():
    filenames = []
    for dir in params.dir_list:
        filenames += glob(f'{path.join(params.dataset_dir, dir)}/**/*.wav', recursive=True)
    
    if not path.exists(path.join(params.main_dir, params.mel_dir)):
        mkdir(path.join(params.main_dir, params.mel_dir))
    
    for dir in params.dir_list:
        if not path.exists(path.join(params.main_dir, params.mel_dir, dir)):
            mkdir(path.join(params.main_dir, params.mel_dir, dir))

    for filename in tqdm(filenames, desc='Preprocessing'):
        transform(Path(filename))


if __name__ == '__main__':
    main()