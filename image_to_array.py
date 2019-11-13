from PIL import Image
import numpy
import sys

def image2pixelarray(filepath):
  """
  Parameters
  ----------
  filepath : str
      Path to an image file

  Returns
  -------
  list
      A list of lists which make it simple to access the greyscale value by
      im[y][x]
  """
  # import code; code.interact(local=dict(globals(), **locals()))
  im = Image.open(filepath[0]).convert('L')
  # (width, height) = im.size
  # greyscale_map = list(im.getdata())
  greyscale_map = numpy.array(im)
  print (greyscale_map)
  import code; code.interact(local=dict(globals(), **locals()))
  # greyscale_map = greyscale_map.reshape((height, width))
  new = Image.fromarray(greyscale_map, 'L')
  new.show()

if __name__ == "__main__":
  image2pixelarray(sys.argv[1:])
