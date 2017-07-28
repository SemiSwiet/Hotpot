"""
A simple dnn model
"""

from __future__ import print_function
from __future__ import division

from keras.layers import Input, TimeDistributed, Dense, Lambda, concatenate, Dropout, BatchNormalization
from keras import backend as K
from keras.regularizers import l2

import pysts.kerasts.blocks as B


def config(c):
    c['l2reg'] = 1e-5

    c['deep'] = 4
    c['nndim'] = 200
    c['nndropout'] = 0.1
    c['nnact'] = 'relu'
    c['nninit'] = 'glorot_uniform'

    # model-external:
    c['inp_e_dropout'] = 1/3
    c['inp_w_dropout'] = 0

    # anssel-specific:
    c['ptscorer'] = B.mlp_ptscorer
    c['mlpsum'] = 'sum'
    c['Ddim'] = 1


def prep_model(inputs, N, s0pad, s1pad, c):
    # Word-level projection before averaging
    inputs[0] = TimeDistributed(Dense(N, activation='relu'))(inputs[0])
    inputs[0] = Lambda(lambda x: K.max(x, axis=1), output_shape=(N, ))(inputs[0])
    inputs[1] = TimeDistributed(Dense(N, activation='relu'))(inputs[1])
    inputs[1] = Lambda(lambda x: K.max(x, axis=1), output_shape=(N, ))(inputs[1])
    merged = concatenate([inputs[0], inputs[1]])
    
    # Deep
    for i in range(c['deep']):
        merged = Dense(c['nndim'], activation=c['nnact'])(merged)
        merged = Dropout(c['nndropout'])(merged)
        merged = BatchNormalization()(merged)

    is_duplicate = Dense(1, activation='sigmoid')(merged)
    return [is_duplicate], N
