#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:15:55 2020

@author: alienor
"""

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
from romiseg.utils.train_from_dataset import init_set, Dataset_im_label
from torchvision import transforms
import toml
import torch


default_config_dir = "/home/alienor/Documents/scanner-meta-repository/Scan3D/config/segmentation2d_arabidopsis.toml"

parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--config', dest='config', default=default_config_dir,
                    help='config dir, default: %s'%default_config_dir)


args = parser.parse_args()


param_pipe = toml.load(args.config)

direc = param_pipe['TrainingDirectory']

path = direc['path']
directory_weights = path + direc['directory_weights']
tsboard = path +  direc['tsboard'] + '/2D_segmentation'
directory_dataset = path + direc['directory_dataset']


param2 = param_pipe['Segmentation2D']
model_name = param2["model_name"]
model_segmentation_name = param2["model_segmentation_name"]

label_names = param2['labels'].split(',')


Sx = param2['Sx']
Sy = param2['Sy']

epochs = param2['epochs']
batch_size = 6

learning_rate = param2['learning_rate']

path_train = directory_dataset + '/train/'

image_train, target_train = init_set('', path_train)

trans = transforms.Compose([
                            transforms.CenterCrop((Sx, Sy)),
                            transforms.ToTensor(),
                            ])

train_dataset = Dataset_im_label(image_train, target_train, transform = trans)


train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=1)
    

g = alien.showclass()

all_data = next(iter(train_loader))
images = all_data[0]
label = all_data[1]
#plot 4 images to visualize the data
images_tot = []
titles_tot = []
for i in range(min(batch_size, len(label_names))):
    img = images[i]
    img = img.permute(1, 2, 0)
    images_tot.append(img)

g.title_list = None
g.save_folder = ''
g.spacing = 0.02
g.figsize = (14.9,10)
g.fontsize = 20
g.save_name = 'vscan_sample'
g.col_num = 3
#g.showing(figure)
g.saving(images_tot)