# Home ProTech Back End
## Existing Development
Currently, this portion of the application is under development. In order to run the image slicing script on a .xyz point cloud file, you can use the git clone command on this repository and then run 

```Python
pip3 install -r requirements.txt
python3 pointcloud_to_array.py -h # This will return the commands needed to run the script.
```

where step is equal to the size of the slice. Lower sizes will grab more slices, but may have almost no points in them, producing almost blank images. Depending on the z-axis values of the point cloud file, you may see very detailed images or very fuzzy images. The number of slices will be determined by the range between the min and max values of the z-axis in the point cloud file. Currently each xyz file requires manual intervention in the script in order to produce images that are useful. This will be automated away in time, however. 

## Future Development
We currently have some of the models needed to process images and point cloud files in order to perform image recognition on them, and we plan to continue development in this direction. Currently we are evaluating the [PointNet++](https://github.com/charlesq34/pointnet2) model for semantic item detection. We are also evaluating using [Facebook House3D](https://github.com/facebookresearch/House3D/blob/master/House3D/house.py) in order to route optimize for escape routes. Route optimization in a house from the firefighters perspective is typically a traveling salesman problem - what's the shortest route to hit all of the livable areas of the house from the different entryways in the least amount of time? This is a well known problem, and we are currently utilizing Q learning to approach the problem from another angle. 

We also plan on implementing a Flask API utilizing a Postgres database in order to serve requests from the React Native front end. This backend would be hosted on a Heroku instance utilizing Heroku Shield, which is a best in class service that provides secure storage for data and is HIPAA compliant.
