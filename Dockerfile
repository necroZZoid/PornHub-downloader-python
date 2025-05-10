FROM ubuntu:latest

# Update package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y python3.7 python3-pip wget git

# Set the working directory in the container
WORKDIR /app

# Clone the repository
RUN git clone https://github.com/necroZZoid/PornHub-downloader-python.git

# Install the Python dependencies directly
RUN pip3 install \
    bs4==0.0.1 \
    prettytable==0.7.2 \
    requests==2.31.0 \
    youtube-dl==2021.06.06 \
    lxml==4.9.4 \
    urllib3 \
    --break-system-packages

WORKDIR /app/PornHub-downloader-python

# Keep the container running (you'll likely want to change this to run the script)
CMD ["tail", "-f", "/dev/null"]
