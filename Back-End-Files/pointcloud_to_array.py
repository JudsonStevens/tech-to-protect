from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d
import sys
import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-fp", "--filepath", required=True, help="This is the filepath to the xyz file")
ap.add_argument("-s", "--step", required=False, help="This is the step to use. Smaller steps generate more files but may compromise image quality")
ap.add_argument("-o", "--output", required=True, help="This is the filepath to output the images")
args = vars(ap.parse_args())

def main():
  pcd = o3d.io.read_point_cloud(args['filepath'], format='xyz')
  xyz_load = np.asarray(pcd.points)
  x_lidar = xyz_load[:, 0]
  y_lidar = xyz_load[:, 1]
  z_lidar = xyz_load[:, 2]
  min_value = min(z_lidar)
  max_value = max(z_lidar)
  original_size = z_lidar.size
  saveto = args['output']
  if args['step']:
    step = float(args['step'])
  else:
    step = 0.5
  while min_value < max_value:
    birds_eye_point_cloud(x_lidar, y_lidar, z_lidar, min_value, max_value, step, original_size, saveto)
    min_value = min_value + step

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
def birds_eye_point_cloud(
                          x_lidar,
                          y_lidar,
                          z_lidar,
                          min_value,
                          max_value,
                          step,
                          original_size,
                          saveto='/render_app/example_img-min_size-',
                          side_range=(-10, 10),
                          fwd_range=(-10, 10),
                          res=0.001,
                          ):
  """ Creates an 2D birds eye view representation of the point cloud data.
      You can optionally save the image to specified filename.

      The side and fwd range values can be modified if needed in order to increase or decrease the size of the image.
  """

  print(f'Minimum value = {min_value}, maximum value = {max_value}')

  # Gather all indices where the z values are outside the range we are specifying by the step.
  first_set = np.where(z_lidar > min_value + step)
  second_set = np.where(z_lidar < min_value)
  indices_to_delete = np.setxor1d(first_set, second_set)

  # Check to make sure the delete process worked.
  if len(indices_to_delete) == 0:
    raise Exception("No indices were found to delete.")

  # Print out the length of the original z list, and the size of the array of indices to delete.
  print(len(z_lidar))
  print(len(indices_to_delete))
  x_lidar = np.delete(x_lidar, indices_to_delete)
  y_lidar = np.delete(y_lidar, indices_to_delete)
  z_lidar = np.delete(z_lidar, indices_to_delete)


  # INDICES FILTER - of values within the desired rectangle
  # Note left side is positive y axis in LIDAR coordinates
  # This should be modified depending on the image.
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
                          a_min=min_value,
                          a_max=(min_value + step))

  # RESCALE THE HEIGHT VALUES - to be between the range 0-255
  pixel_values  = scale_to_255(pixel_values, min=min_value, max=(min_value + step))

  # FILL PIXEL VALUES IN IMAGE ARRAY
  x_max = int((side_range[1] - side_range[0])/res)
  y_max = int((fwd_range[1] - fwd_range[0])/res)
  im = np.zeros([y_max, x_max], dtype=np.uint8)
  im[-y_img, x_img] = pixel_values # -y because images start from top left

  print(z_lidar.size)
  print(original_size)
  if im.size > (original_size * .25):
  # Convert from numpy array to a PIL image
    im = Image.fromarray(im)
    im.save(saveto + f'{round(min_value, 2)}.jpeg')
  else:
    print("Array was too small.")

if __name__ == "__main__":
  main()
