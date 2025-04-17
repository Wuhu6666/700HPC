#!/bin/bash
#SBATCH --job-name=sorting_benchmark
#SBATCH --partition=intel
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=16
#SBATCH --mem=50G
#SBATCH --time=12:00:00
#SBATCH --output=sorting_%j.out
#SBATCH --error=sorting_%j.err
#SBATCH --constraint=del_int_16_256

# Set working directory
cd /moosefs/home/s265d007/projects/700HPC

# Run the Python script
python3 parallelwrapper.py

cat results_*.txt > all_results.txt