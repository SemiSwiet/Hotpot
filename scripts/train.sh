#! /bin/bash
# format: MODEL TASK TRAIN_FILE VAL_FILE 

python3 tools/train.py gran para data/question-pairs-dataset/train-small.csv \
data/question-pairs-dataset/test.csv epochs=1
