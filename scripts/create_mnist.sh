#!/usr/bin/env sh
# This script converts the mnist data into lmdb/leveldb format,
# depending on the value assigned to $BACKEND.

EXAMPLE=./
DATA=~/Caffe/data/mnist
BUILD=~/Caffe/build/examples/mnist

BACKEND="lmdb"

echo "Creating ${BACKEND}..."

rm -rf $EXAMPLE/mnist_test_${BACKEND}

$BUILD/convert_mnist_data.bin $DATA/t10k-images-idx3-ubyte \
  $DATA/t10k-labels-idx1-ubyte $EXAMPLE/mnist_test_${BACKEND} --backend=${BACKEND}

echo "Done."
