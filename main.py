from Astro import *
from readheader import *

before_bin_stack_path = 'images/M_31_wizardstack_222f.fits'
#after_bin_stack_path = 'images/NGC7000_120s_200Gain_Stacked_AfterBinning.fit'
single_path = 'images/Light_M 31_60.0s_Bin1_gain200_20261016-225207_8deg_-10.0C_0005.fit'

single_noise = analyze_fits(single_path)


before_bin_results = analyze_fits(file_path= before_bin_stack_path, is_stack=True, single_frame_noise=single_noise)
# print(before_bin_results)


#analyze_stack(before_bin_stack_path)