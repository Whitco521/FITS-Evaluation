from math import exp
import numpy as np
from astropy.io import fits
from astropy.stats import median_absolute_deviation, sigma_clipped_stats
from astropy.table import Table
from photutils.detection import DAOStarFinder, IRAFStarFinder
import pandas as pd



def analyze_stack (file_path):
    with fits.open(file_path) as hdul:
        data = hdul[0].data.astype(float)
        print(fits.getheader(file_path))