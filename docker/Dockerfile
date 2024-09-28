# BASE segnet
FROM debian:12 AS caffe-segnet-base

RUN sed -i 's#main#main contrib non-free non-free-firmware#g' /etc/apt/sources.list.d/debian.sources
RUN apt-get update -y
RUN apt-get install -y --no-install-recommends make g++ curl git ca-certificates

WORKDIR /app
RUN git clone https://github.com/MPIB/caffe-segnet.git
WORKDIR /app/caffe-segnet


# GPU version of segnet
FROM caffe-segnet-base AS caffe-segnet-gpu

ADD Makefile.config.gpu Makefile.config
RUN apt-get install -y --no-install-recommends nvidia-cuda-toolkit nvidia-cuda-dev
RUN curl -o /tmp/cuda.tgz https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-10.1-linux-x64-v7.6.5.32.tgz
RUN tar xfz /tmp/cuda.tgz -C /usr/local
RUN mv /usr/local/cuda /usr/local/cudnn
RUN apt-get install -y --no-install-recommends libopencv-core-dev libprotobuf-dev libopenblas-openmp-dev libhdf5-dev libleveldb-dev liblmdb-dev libopencv-highgui-dev libboost1.74-dev libboost-thread-dev libboost-filesystem-dev libboost-python-dev protobuf-compiler libgflags-dev libgoogle-glog-dev libsnappy-dev libpython3-dev python3-numpy
RUN apt-get install -y --no-install-recommends libsnappy1v5 libopenblas0-openmp libboost-thread1.74.0 libboost-filesystem1.74.0 libboost-python1.74.0
RUN make -j12
RUN make pycaffe distribute

# CPU version of segnet
FROM caffe-segnet-base AS caffe-segnet-cpu

ADD Makefile.config.cpu Makefile.config
RUN apt-get install -y --no-install-recommends nvidia-cuda-toolkit nvidia-cuda-dev
RUN curl -o /tmp/cuda.tgz https://developer.download.nvidia.com/compute/redist/cudnn/v7.6.5/cudnn-10.1-linux-x64-v7.6.5.32.tgz
RUN tar xfz /tmp/cuda.tgz -C /usr/local
RUN mv /usr/local/cuda /usr/local/cudnn
RUN apt-get install -y --no-install-recommends libopencv-core-dev libprotobuf-dev libopenblas-openmp-dev libhdf5-dev libleveldb-dev liblmdb-dev libopencv-highgui-dev libboost1.74-dev libboost-thread-dev libboost-filesystem-dev libboost-python-dev protobuf-compiler libgflags-dev libgoogle-glog-dev libsnappy-dev libpython3-dev python3-numpy
RUN apt-get install -y --no-install-recommends libsnappy1v5 libopenblas0-openmp libboost-thread1.74.0 libboost-filesystem1.74.0 libboost-python1.74.0
RUN make -j12
RUN make pycaffe distribute

# target image with both segnet libraries installed
FROM debian:12

COPY --from=caffe-segnet-cpu /app/caffe-segnet/distribute /usr/local/caffe-cpu
COPY --from=caffe-segnet-gpu /app/caffe-segnet/distribute /usr/local/caffe-gpu
COPY --from=caffe-segnet-gpu /usr/local/cudnn /usr/local/cudnn

RUN sed -i 's#main#main contrib non-free non-free-firmware#g' /etc/apt/sources.list.d/debian.sources
RUN apt-get update -y && apt-get install -y --no-install-recommends libopencv-core406 libopencv-highgui406 libopencv-imgcodecs406 \
                                                                    libprotobuf32 libopenblas0-openmp libhdf5-103 libleveldb1d liblmdb0 \
                                                                    libboost1.74 libgflags2.2 libgoogle-glog0v6 libcudart11.0 libcublas11 libcurand10
RUN apt-get install -y --no-install-recommends git ca-certificates python3-pip python3-wheel python3-venv
WORKDIR /app
RUN git clone --depth 1 https://github.com/MPIB/GSV2SVF /app && rm -rf /app/.git
RUN bash -c 'cat /app/SegNet*/Example*/*webdemo_{1,2,3}* > /app/SegNet-Tutorial-master/Example_Models/segnet_weights_driving_webdemo.caffemodel' \
    && bash -c 'rm -f /app/SegNet*/Example*/*webdemo_{1,2,3}*'
RUN python3 -m venv env
RUN /app/env/bin/pip3 install -r requirements.txt
ENV SVFHOME=/app/
ADD env.sh /env.sh
ENTRYPOINT ["sh", "-c", ". /env.sh && \"$@\"", "-s"]
CMD ["/app/env/bin/python3", "/app/RunTaskSimple.py"]
