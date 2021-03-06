#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 14:20:37 2020

@author: alienor
"""

import numpy as np
import romiseg.utils.alienlab as alien
import imageio
import argparse
import matplotlib.gridspec as gridspec

default_path = '/home/alienor/Documents/training2D/data/dataset_gl_png/train/000018'


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--config', dest='config', default=default_path,
                    help='config dir, default: %s'%default_path)


args = parser.parse_args()


path = args.config

classes = ['background', 'stem', 'leaf', 'fruit', 'pedicel']

image_path = '/images/00001_rgb.png'
labels_path = {}
for c in classes: 
    labels_path[c] = '/images/00001_%s.png'%c


g = alien.showclass()

image = imageio.imread(path + image_path)


figure = [image]


for c in classes:
        label = imageio.imread(path + labels_path[c])
        figure.append(label)


g.title_list = None#['Image' , 'Flower', 'Peduncle', 'Stem', 'Leaf', 'Fruit']
#['Image', 'Background' , 'Flower', 'Peduncle', 'Stem', 'Leaf', 'Fruit']
g.save_folder = ''
g.spacing = 0.02
g.figsize = (14.9,10)
g.fontsize = 20
g.extension = ".png"

g.save_name = 'Images_and_labels'
g.col_num = 3
#g.showing(figure)
g.saving(figure)