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

default_path = '/home/alienor/Documents/database/tomato_paper/'


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--config', dest='config', default=default_path,
                    help='config dir, default: %s'%default_path)


args = parser.parse_args()


path = args.config

classes = ['background', 'stem', 'leaf', 'pedicel']

image_path = '/images/0.jpg'
labels_path = {}
for c in classes: 
    labels_path[c] = '/Segmentation2D_896_896_ModelFileset_2513428f8c/000_%s.png'%c


g = alien.showclass()

image = imageio.imread(path + image_path)


figure = [image]


for c in ['background','stem', 'leaf']:
    if c == 'stem':
        label = imageio.imread(path + labels_path[c]) + imageio.imread(path + labels_path['pedicel'])
    else: 
        label = imageio.imread(path + labels_path[c])
    figure.append(label)


g.title_list = None#['Image' , 'Flower', 'Peduncle', 'Stem', 'Leaf', 'Fruit']
#['Image', 'Background' , 'Flower', 'Peduncle', 'Stem', 'Leaf', 'Fruit']
g.save_folder = ''
g.spacing = 0.02
g.figsize = (14.9,10)
g.fontsize = 20
g.extension = ".png"

g.col_num = 2
#g.showing(figure)
g.saving(figure)