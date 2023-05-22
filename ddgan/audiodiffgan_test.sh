#!/bin/bash

python3 test_ddgan.py \
    --dataset SC09 \
    --image_size 128 \
    --exp ddgan_SC09_exp3_4steps \
    --num_channels 1 \
    --num_channels_dae 64 \
    --ch_mult 1 1 2 2 4 4 \
    --num_timesteps 4 \
    --num_res_blocks 2 \
    --epoch_id 400 \
    --batch_size 1