import matplotlib.pyplot as plt
from torch import Tensor, transpose
import librosa.display


def plot_melspecs(c_fake: Tensor, n=8, tags=''):
    """ `c_fake` (bs, seq_len, c_dim) """
    fig, axs = plt.subplots(nrows=2, ncols=4, figsize=(15, 7))
    axs = axs.flatten()
    c_fake = transpose(c_fake, 1, 2)
    for i in range(min(n, c_fake.shape[0])):
        librosa.display.specshow(c_fake[i].T.cpu().numpy(), cmap='viridis', ax=axs[i], vmin=-11.4, vmax=2.5)
    fig.tight_layout()
    plt.savefig(f'mel_samples{tags}.png')