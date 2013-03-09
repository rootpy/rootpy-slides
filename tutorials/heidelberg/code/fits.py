import numpy as np
data = np.random.random(size=1000)

from astropy.io import fits
fits.writeto('data.fits', data) # Write array to FITS file
data2 = fits.getdata('data.fits') # Read data from FITS file
