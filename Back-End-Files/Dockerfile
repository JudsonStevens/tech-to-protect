FROM python:3.7
ARG export_file=3d_render.xyz
WORKDIR /export_data
COPY $export_file 3d_render.xyz
RUN pip3 install
CMD ["python", "./process_3d_render.py"]
