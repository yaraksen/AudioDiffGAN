from pathlib import Path
import math
import random
import numpy as np
import torch
import torch.nn.functional as F
import os
from os import glob

from torch.utils.data import Dataset

import torchaudio
import torchaudio.transforms as transforms


class MelDataset(Dataset):
    def __init__(self, mels_dir: str, train: bool = True):
        self.train = train
        self.filenames = glob(f'{mels_dir}/**/*.wav', recursive=True)

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        spec_filename = self.filenames[idx]
        spectrogram = np.load(spec_filename)
        return spectrogram

