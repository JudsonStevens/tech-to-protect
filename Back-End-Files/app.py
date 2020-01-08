from flask import Flask, jsonify, request, render_template, redirect, url_for
from pointcloud_to_array import main
import os, boto3

# Application
app = Flask(__name__)

# Methods
def process_model(file_path):
  # Logic to process the render file if it's an xyz by the model
  main(file_path)

def generate_2d_floorplan(render_file):


# Routes
@app.route('/input3dRender', methods=['POST'])
def process_render_file():
  render_file = request.files['render_file']
  try:
    if render_file.split('.')[1] == 'xyz':
        render_file.save('/var/www/uploads/render_file.xyz')
        process_model(file_path)
        generate_2d_floorplan(file_path)
  except:
    output = {'message': 'The file upload was unsuccessful.'}
    return jsonify(results=output)
  # Logic to process render file by the predictive/item detection model


if __name__ == '__main__':
  app.run()