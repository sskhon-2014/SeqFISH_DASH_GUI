from pre_processing import *
from pathlib import Path
import os
from webfish_tools.util import find_matching_files
import re
import numpy as np

JOB_ID = os.getenv('SLURM_ARRAY_TASK_ID', 0)

print(f'This is task {JOB_ID}')

#paths for real image
directory = Path('$FILENAME$')
position_name = f'MMStack_Pos{JOB_ID}.ome.tif'

files, _, _ = find_matching_files(directory, 'HybCycle_{hyb}' + f'/{position_name}')
files = [str(f) for f in files]

#-----------------------------------------------------------------------

#correction function and arguments
correction_type=Guassian_E
swapaxes=False
stack_bkgrd=None
z=1
size=$DIMENSION$
gamma = 1.2
sigma=30
rb_radius=5
hyb_offset=0
rollingball=False
lowpass = False
match_hist=False
subtract=False
divide=False

correct_many(files, correction_type, stack_bkgrd, swapaxes, z, size, gamma, 
             sigma, rb_radius, hyb_offset, rollingball, lowpass, match_hist, subtract, divide)