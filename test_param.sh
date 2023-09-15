#!/bin/bash


Oplevel=$1

unroll=$2

bo=$3

bp=$4

gcc -g -O${Oplevel} test.c -o test --param=max-unroll-times=${unroll} --param=predictable-branch-outcome=${bo} --param=tracer-min-branch-probability=${bp} -frecord-gcc-switches