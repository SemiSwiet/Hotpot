#! /bin/bash
# format: MODEL TASK TRAIN_FILE VAL_FILE 

python3 tools/train.py avg para data/question-pairs-dataset/train-xxsmall.csv  \
data/question-pairs-dataset/train-xxsmall.csv 
