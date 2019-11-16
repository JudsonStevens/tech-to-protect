# Home ProTech Back End
## Existing Development
Currently, this portion of the application is under development. In order to run the image slicing script on a .xyz point cloud file, you can use the git clone command on this repository and then run `python3 pointcloud_to_array.py "[path/to/the/pointcloud]" [step]` where step is equal to the size of the slice. Lower sizes will grab more slices, but may have almost no points in them, producing almost blank images. Depending on the z-axis values of the point cloud file, you may see very detailed images or very fuzzy images. 
