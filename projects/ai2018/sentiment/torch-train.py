#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# ==============================================================================
#          \file   train.py
#        \author   chenghuige  
#          \date   2018-01-13 16:32:26.966279
#   \Description  
# ==============================================================================
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys, os

import tensorflow as tf 
flags = tf.app.flags
FLAGS = flags.FLAGS

import numpy as np
from tqdm import tqdm

import melt 
logging = melt.logging
import gezi
import traceback

from wenzheng.utils import input_flags 

#from algos.model import *
from torch_algos.loss import criterion
import torch_algos.model as base
from dataset import Dataset
import evaluate as ev

def main(_):
  FLAGS.num_folds = 8
  FLAGS.torch = True
  melt.apps.init()
  
  ev.init()

  model = getattr(base, FLAGS.model)()

  logging.info(model)

  train = melt.apps.get_train()

  train(Dataset,
        model,  
        criterion,
        eval_fn=ev.calc_f1, 
        valid_write_fn=ev.valid_write,
        infer_write_fn=ev.infer_write,
        valid_suffix='.valid.csv',
        infer_suffix='.infer.csv')   

if __name__ == '__main__':
  tf.app.run()  
