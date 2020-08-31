# =======================================
# This is an automatically generated file.
# =======================================
FROM tensorflow/tensorflow:2.3.0-gpu

# Update pip and install all pip dependencies
RUN /usr/bin/python3 -m pip install --upgrade pip
COPY ./docker/requirements.txt /opt/project/requirements.txt
RUN pip install -r /opt/project/requirements.txt

# Copy the resources folder
COPY ./resources /opt/project/resources

# Copy full project (sources + tests). This does *NOT* include the mount folder.
COPY ./my_project /opt/project/my_project
COPY ./tests /opt/project/tests
