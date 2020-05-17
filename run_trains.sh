#!/bin/bash

#### new datasets for training ###
# dataset internal
#python main_train.py --config config_lstm.json --dataset "/data/track-ml/eramia/results/eta_n0.5-0.5_phi_n0.5-0.5.csv" --cylindrical False
#python main_train.py --config config_lstm.json --dataset "/data/track-ml/eramia/results/eta_n0.5-0.5_phi_n0.5-0.5.csv" --cylindrical True

# dataset intermediary
#python main_train.py --config config_lstm.json --dataset "/data/track-ml/eramia/results/eta_0.0-1.0_phi_0.0-1.0.csv " --cylindrical False
#python main_train.py --config config_lstm.json --dataset "/data/track-ml/eramia/results/eta_0.0-1.0_phi_0.0-1.0.csv " --cylindrical True

# dataset external
python main_train.py --config config_lstm.json --dataset "/data/track-ml/eramia/dataset/eta_n0.5-0.5_phi_ninf-pinf.csv" --cylindrical True
python main_train.py --config config_lstm.json --dataset "/data/track-ml/eramia/dataset/eta_n0.5-0.5_phi_ninf-pinf.csv" --cylindrical False