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

        return wav, logmel
