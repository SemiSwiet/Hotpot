#! /bin/bash
# format: MODEL TASK TRAIN_FILE VAL_FILE 

python3 tools/train.py gran para data/train-xxsmall.csv  \
data/train-xxsmall.csv 
