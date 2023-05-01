from pathlib import Path
import math
import random
import numpy as np
import torch
import torch.nn.functional as F

from torch.utils.data import Dataset

import torchaudio
import torchaudio.transforms as transforms



class MelDataset(Dataset):
    def __init__(
        self,
        root: Path,
        train: bool = True
    ):
        self.mels_dir = root / "mels"
        self.train = train

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
