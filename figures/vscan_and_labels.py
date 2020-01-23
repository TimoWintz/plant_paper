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

default_path = '/home/alienor/Documents/training2D/data/dataset_stem_green/train/arabidopsis_1'


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--config', dest='config', default=default_path,
                    help='config dir, default: %s'%default_path)


args = parser.parse_args()


path = args.config


image_path = '/images/00000_rgb.jpg'
labels_path = '/images/00000_segmentation.npz'


g = alien.showclass()

image = imageio.imread(path + image_path)
labels = np.load(path + labels_path)


figure = []


for i in range(len(labels.files)):
    if i != 3:
        label = labels[labels.files[i]]
        figure.append(label)

    
#tmp = np.stac(figure, axis = 0)
somme = np.sum(figure, axis = 0)
background = somme == 0
background = background
background = background
dimx, dimy = background.shape
#figure = [image, background] + figure
figure = [image] + figure


g.title_list = None#['Image' , 'Flower', 'Peduncle', 'Stem', 'Leaf', 'Fruit']
#['Image', 'Background' , 'Flower', 'Peduncle', 'Stem', 'Leaf', 'Fruit']
g.save_folder = ''
g.spacing = 0.02
g.figsize = (14.9,10)
g.fontsize = 20
g.save_name = 'Images_and_labels'
g.col_num = 3
#g.showing(figure)
g.saving(figure)