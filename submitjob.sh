#!/bin/bash
#SBATCH --job-name=sorting_benchmark_g019_r28c4_upto5m
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=50G
#SBATCH --time=23:00:00
#SBATCH --output=sorting_%j.out
#SBATCH --error=sorting_%j.err
#SBATCH --constraint=r28c4

# Set working directory
cd /moosefs/home/s265d007/projects/git2/700HPC

# Run the Python script
python3 parallelwrapper.py

cat results_*.txt > all_results.txt