#!/bin/bash

#SBATCH --job-name=sorting_benchmark_g016_gpu_32cores_gpu_1
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=32
#SBATCH --mem=60G
#SBATCH --time=23:00:00
#SBATCH --output=sorting_%j.out
#SBATCH --error=sorting_%j.err
#SBATCH --constraint=gpu,eth_10g,r27c1

cd /moosefs/home/s265d007/projects/git2/700HPC

python3 wrapper.py