import numpy as np


class AttrDict(dict):
  def __init__(self, *args, **kwargs):
      super(AttrDict, self).__init__(*args, **kwargs)
      self.__dict__ = self

  def override(self, attrs):
    if isinstance(attrs, dict):
      self.__dict__.update(**attrs)
    elif isinstance(attrs, (list, tuple, set)):
      for attr in attrs:
        self.override(attr)
    elif attrs is not None:
      raise NotImplementedError
    return self


params = AttrDict(
    # mel params
    sample_rate = 16000,
    num_frames = 16000,
    n_fft = 1024,
    win_length = 1024,
    hop_length = 160,
    center=False,
    power=1.0,
    norm="slaney",
    onesided=True,
    n_mels=128,
    mel_scale="slaney",

    # datasets
    dir_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'],
    dataset_dir = '/home/yaoaksyonov/coursework/SC_dataset',
    main_dir = '/home/yaoaksyonov/coursework/audio_diff_gan',
    mel_dir = 'mels',

    audio_len = 16000
)
