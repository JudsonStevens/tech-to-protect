# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:03:41 2019

@author: Stephanie
"""

%matplotlib inline
import os
from glob import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

read_xyz_data = lambda path, rows: pd.read_table(path, sep = ' ', nrows = rows, names = ['x', 'y', 'z',  'r', 'g','b'], header = None)
read_xyz_data('SD2_full_home_simplified_1cm.xyz', :)

def preprocess_point_cloud(point_cloud):
    ''' Prepare the numpy point cloud (N,3) for forward pass '''
    point_cloud = point_cloud[:,0:3] # do not use color for now
    floor_height = np.percentile(point_cloud[:,2],0.99)
    height = point_cloud[:,2] - floor_height
    point_cloud = np.concatenate([point_cloud, np.expand_dims(height, 1)],1) # (N,4) or (N,7)
    point_cloud = random_sampling(point_cloud, FLAGS.num_point)
    pc = np.expand_dims(point_cloud.astype(np.float32), 0) # (1,40000,4)
    return pc


fig, m_axs = plt.subplots(1, 3, figsize = (20, 5))
ax_names = 'xyz'
for i, c_ax in enumerate(m_axs.flatten()):
    plot_axes = [x for j, x in enumerate(ax_names) if j!=i]
    c_ax.scatter(df[plot_axes[0]],
                df[plot_axes[1]],
                c=df[['r', 'g', 'b']].values/255, 
                 s=1
                )
    c_ax.set_xlabel(plot_axes[0])
    c_ax.set_ylabel(plot_axes[1])

fig = plt.figure(figsize=(15,10))
ax = plt.axes(projection='3d')
ax.scatter(
            df['x'], df['y'], df['z'],
            c=df[['r', 'g', 'b']].values/255, s=3)  
ax.view_init(15, 165)



fig = plt.figure(figsize=(15,10))
ax = plt.axes(projection='3d')
ax.scatter(
            test_df['x'], test_df['y'], test_df['z'],
            c=test_df[['r', 'g', 'b']].values/255, s=3)  
ax.view_init(15, 165)

ax.view_init(45, 220)
fig.savefig('3D_rendering.png', dpi = 300)
fig


fig = plt.figure(figsize=(15,10))
ax = plt.axes(projection='3d')  
for (c_key, c_value) in label_names.items():
    c_df = test_df[test_df['class']==c_key]
    ax.plot(c_df['x'], c_df['y'], c_df['z'], '.', label = c_value, alpha = 0.5)  
ax.legend()
ax.view_init(15, 165)
fig.savefig('3d_labels.png', dpi = 300)


