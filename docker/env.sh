[ "$CAFFE_BLEND" != "cpu" ] && [ "$CAFFE_BLEND" != "gpu" ] && echo "CAFFE_BLEND=[gpu|cpu] environment is required" && exit 1

export PYTHONPATH=/usr/local/caffe-$CAFFE_BLEND/python
export LD_LIBRARY_PATH=/usr/local/caffe-$CAFFE_BLEND/lib:/usr/local/cudnn/lib64
