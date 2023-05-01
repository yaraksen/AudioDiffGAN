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

    audio = torch.clamp(audio[0], -1.0, 1.0)

    if audio.size(-1) < params.num_frames:
        audio = F.pad(audio, (0, params.num_frames - audio.size(-1)))

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
        # audio = F.pad(audio, ((1024 - 160) // 2, (1024 - 160) // 2), "reflect")

        spectrogram = mel_spec_transform(audio)
        spectrogram = torch.log(torch.clamp(spectrogram, min=1e-5))

        # preprocessing from DiffWave
        # spectrogram = 20 * torch.log10(torch.clamp(spectrogram, min=1e-5)) - 20
        # spectrogram = torch.clamp((spectrogram + 100) / 100, 0.0, 1.0)

        np.save(f'{params.main_dir}/mels/{filename.stem}.spec.npy', spectrogram.cpu().numpy())


def main():
    # one should delete noise data and anything from 0-9 numbers
    filenames = []
    for dir in params.dir_list:
        filenames += glob(f'{path.join(params.dataset_dir, dir)}/**/*.wav', recursive=True)
    
    if not path.exists(params.main_dir + '/mels'):
        mkdir(params.main_dir + '/mels')

    for filename in tqdm(filenames, desc='Preprocessing'):
        transform(Path(filename))


if __name__ == '__main__':
    main()
