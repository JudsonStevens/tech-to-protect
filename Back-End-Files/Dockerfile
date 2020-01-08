FROM python:3.7
ARG EXPORT_FILE=3d_render.xyz
ARG STEP=1
COPY $export_file 3d_render.xyz
COPY requirements.txt requirements.txt
WORKDIR /render_app
VOLUME /render_app
RUN pip3 install -r requirments.txt
RUN python3 ./process_3d_render ${EXPORT_FILE}} ${STEP}
# CMD ["python", "./process_3d_render.py"]
