This is a fork of (the fork) https://github.com/NewSoupVi/GSV2SVF-reduced . It's a decluttered and modified version to support cudnn7 and more recent GPUs. It builds on Debian 12 and comes with a simple Dockerfile.

### Docker

There are two variants inside the image and you switch between cpu and gpu version using a `CAFFE_BLEND` environment variable:

Build it:

```sh
git clone https://github.com/MPIB/GSV2SVF
cd GSV2SVF/docker
docker build -t gsv2svf:latest .
```


```sh
docker run -it --rm -e "CAFFE_BLEND=cpu" -v PATH/TO/TASK:/task gsv2svf:latest /task
```

### Apptainer (Singularity)

```sh
apptainer build container.sif docker-daemon://gsv2svf:latest
```

```sh
apptainer run --nv --env "CAFFE_BLEND=gpu" -B PATH/TO/TASK:/task container.sif /task
```
