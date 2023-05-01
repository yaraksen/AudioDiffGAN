from pathlib import Path
import math
import random
import numpy as np
import torch
import torch.nn.functional as F

from torch.utils.data import Dataset

import torchaudio
import torchaudio.transforms as transforms


class LogMelSpectrogram(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.melspectrogram = transforms.MelSpectrogram(
            sample_rate=16000,
            n_fft=1024,
            win_length=1024,
            hop_length=160,
            center=False,
            power=1.0,
            norm="slaney",
            onesided=True,
            n_mels=128,
            mel_scale="slaney",
        )

    def forward(self, wav):
        wav = F.pad(wav, ((1024 - 160) // 2, (1024 - 160) // 2), "reflect")
        mel = self.melspectrogram(wav)
        logmel = torch.log(torch.clamp(mel, min=1e-5))
        return logmel


class MelDataset(Dataset):
    def __init__(
        self,
        root: Path,
        segment_length: int,
        sample_rate: int,
        train: bool = True
    ):
        self.wavs_dir = root / "wavs"
        self.mels_dir = root / "mels"
        self.data_dir = self.mels_dir

        self.segment_length = segment_length
        self.sample_rate = sample_rate
        self.train = train

        suffix = ".wav" if not finetune else ".npy"
        pattern = f"train/**/*{suffix}" if train else "dev/**/*{suffix}"

        self.metadata = [
            path.relative_to(self.data_dir).with_suffix("")
            for path in self.data_dir.rglob(pattern)
        ]

        self.logmel = LogMelSpectrogram()

    def __len__(self):
        return len(self.metadata)

    def __getitem__(self, index):
        path = self.metadata[index]
        wav_path = self.wavs_dir / path

        info = torchaudio.info(wav_path.with_suffix(".wav"))

        if info.sample_rate != self.sample_rate:
            raise ValueError(
                f"Sample rate {info.sample_rate} doesn't match target of {self.sample_rate}"
            )

        if info.num_frames != self.num_frames:
            raise ValueError(
                f"Number of frames {info.num_frames} doesn't match target of {self.num_frames}"
            )

        wav, _ = torchaudio.load(
            filepath=wav_path.with_suffix(".wav")
        )

        wav = torch.clamp(wav[0], -1.0, 1.0)

        # if wav.size(-1) < self.segment_length:
        #    wav = F.pad(wav, (0, self.segment_length - wav.size(-1)))

        #if self.train:
        #    gain = random.random() * (0.99 - 0.4) + 0.4
        #    flip = -1 if random.random() > 0.5 else 1
        #    wav = flip * gain * wav / wav.abs().max()

        logmel = self.logmel(wav.unsqueeze(0)).squeeze(0)

        return wav, logmel
