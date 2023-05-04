#!/bin/bash

python3 train_ddgan.py \
    --dataset SC09 \
    --image_size 128 \
    --exp ddgan_SC09_exp1 \
    --num_channels 1 \
    --num_channels_dae 64 \
    --ch_mult 1 1 2 2 4 4 \
    --num_timesteps 2 \
    --num_res_blocks 2 \
    --batch_size 4 \
    --num_epoch 500 \
    --ngf 64 \
    --embedding_type positional \
    --use_ema \
    --r1_gamma 2. \
    --z_emb_dim 256 \
    --lr_d 1e-4 \
    --lr_g 2e-4 \
    --lazy_reg 10 \
    --num_process_per_node 2 \
    --save_content \
    --save_ckpt_every 20