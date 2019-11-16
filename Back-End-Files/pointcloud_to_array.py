from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import sys

def main(filepath):
  pcd = o3d.io.read_point_cloud(filepath[0], format='xyz')
  xyz_load = np.asarray(pcd.points)
  birds_eye_point_cloud(xyz_load)

# ==============================================================================
#                                                                   SCALE_TO_255
# ==============================================================================
def scale_to_255(a, min, max, dtype=np.uint8):
    """ Scales an array of values from specified min, max range to 0-255
        Optionally specify the data type of the output (default is uint8)
    """
    return (((a - min) / float(max - min)) * 255).astype(dtype)
# ==============================================================================
#                                                          BIRDS_EYE_POINT_CLOUD
# ==============================================================================
def birds_eye_point_cloud(points,
                          side_range=(-10, 10),
                          fwd_range=(-10,10),
                          res=0.001,
                          min_height = -1,
                          max_height = 1,
                          saveto='/home/judson/Documents/example_img#32.jpeg'):
  """ Creates an 2D birds eye view representation of the point cloud data.
      You can optionally save the image to specified filename.
  """
  x_lidar = points[:, 0]
  y_lidar = points[:, 1]
  z_lidar = points[:, 2]
  # r_lidar = points[:, 3]  # Reflectance
  min_value = min(z_lidar)
  max_value = max(z_lidar)
  print(f'Minimum value = {min_value}, maximum value = {max_value}')
  first_set = np.where(z_lidar > max_value - 3)
  second_set = np.where(z_lidar < min_value + 3)
  indices_to_delete = np.setxor1d(first_set, second_set)
  # indices_to_delete = np.where(np.logical_and((z_lidar > (max_value - 3.5)), (z_lidar < min_value + 3)))
  if len(indices_to_delete) == 0:
    raise Exception("No indices were found to delete.")
  print(indices_to_delete)
  print(len(z_lidar))
  print(len(indices_to_delete))
  x_lidar = np.delete(x_lidar, indices_to_delete)
  y_lidar = np.delete(y_lidar, indices_to_delete)
  z_lidar = np.delete(z_lidar, indices_to_delete)

  print(len(z_lidar))
  # INDICES FILTER - of values within the desired rectangle
  # Note left side is positive y axis in LIDAR coordinates
  ff = np.logical_and((x_lidar > fwd_range[0]), (x_lidar < fwd_range[1]))
  ss = np.logical_and((y_lidar > -side_range[1]), (y_lidar < -side_range[0]))
  indices = np.argwhere(np.logical_and(ff,ss)).flatten()

  # CONVERT TO PIXEL POSITION VALUES - Based on resolution
  x_img = (-y_lidar[indices]/res).astype(np.int32) # x axis is -y in LIDAR
  y_img = (x_lidar[indices]/res).astype(np.int32)  # y axis is -x in LIDAR
                                                    # will be inverted later

  # SHIFT PIXELS TO HAVE MINIMUM BE (0,0)
  # floor used to prevent issues with -ve vals rounding upwards
  x_img -= int(np.floor(side_range[0]/res))
  y_img -= int(np.floor(fwd_range[0]/res))
  
  # CLIP HEIGHT VALUES - to between min and max heights
  pixel_values = np.clip(a = z_lidar[indices],
                          a_min=min_height,
                          a_max=max_height)
  # RESCALE THE HEIGHT VALUES - to be between the range 0-255
  pixel_values  = scale_to_255(pixel_values, min=min_height, max=max_height)

  # FILL PIXEL VALUES IN IMAGE ARRAY
  x_max = int((side_range[1] - side_range[0])/res)
  y_max = int((fwd_range[1] - fwd_range[0])/res)
  im = np.zeros([y_max, x_max], dtype=np.uint8)
  im[-y_img, x_img] = pixel_values # -y because images start from top left
  # im = np.clip()
  # return im
  # Convert from numpy array to a PIL image
  im = Image.fromarray(im)

  # import code; code.interact(local=dict(globals(), **locals()))
  im.save(saveto)
  # SAVE THE IMAGE
  # if saveto is not None:

  # else:
  #   im.show()

if __name__ == "__main__":
  main(sys.argv[1:])

'''
  Args:
      points:     (numpy array)
                  N rows of points data
                  Each point should be specified by at least 3 elements x,y,z
      side_range: (tuple of two floats)
                  (-left, right) in metres
                  left and right limits of rectangle to look at.
      fwd_range:  (tuple of two floats)
                  (-behind, front) in metres
                  back and front limits of rectangle to look at.
      res:        (float) desired resolution in metres to use
                  Each output pixel will represent an square region res x res
                  in size.
      min_height:  (float)(default=-2.73)
                  Used to truncate height values to this minumum height
                  relative to the sensor (in metres).
                  The default is set to -2.73, which is 1 metre below a flat
                  road surface given the configuration in the kitti dataset.
      max_height: (float)(default=1.27)
                  Used to truncate height values to this maximum height
                  relative to the sensor (in metres).
                  The default is set to 1.27, which is 3m above a flat road
                  surface given the configuration in the kitti dataset.
      saveto:     (str or None)(default=None)
                  Filename to save the image as.
                  If None, then it just displays the image.
'''