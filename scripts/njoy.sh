#!/bin/sh

###########################################
#
# script for running batch jobs on Kilkenny
#
###########################################

#PBS -l nodes=1:ppn=1
#PBS -l walltime=23:59:00
#PBS -j oe
#PBS -V

export LD_LIBRARY_PATH=/opt/gcc/4.9.0/lib64:/opt/mpich/3.1.2-gnu/lib

echo $EXE
echo $NJI
echo $TARGET_DIR

cd $TARGET_DIR
$EXE < $NJI
