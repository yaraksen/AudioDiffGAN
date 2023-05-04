from pathlib import Path
import math
import random
import numpy as np
import torch
import torch.nn.functional as F
import os
from os import glob

from torch.utils.data import Dataset
from torchvision.datasets.vision import VisionDataset

import torchaudio
import torchaudio.transforms as transforms

class_to_tgt = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9
}


class MelDataset(VisionDataset):
    def __init__(self, mels_dir: str, train: bool = True):
        self.train = train
        self.targets = []
        self.filenames = []

        for dir in os.listdir(f'{mels_dir}'):
            class_filenames = glob(f'{mels_dir}/{dir}/**/*.spec.npy', recursive=True)
            self.targets += [class_to_tgt[dir]] * len(class_filenames)
            self.filenames += class_filenames
            print(f'in {dir}: target={class_to_tgt[dir]}, len={len(class_filenames)}')

        assert(len(self.filenames) == len(self.targets))
        print('created dataset: ', len(self.filenames))

    def __len__(self):
        return len(self.filenames)

    def __getitem__(self, idx):
        spec_filename = self.filenames[idx]
        spectrogram = torch.from_numpy(np.load(spec_filename))
        target = self.targets[idx]
        return spectrogram, target
