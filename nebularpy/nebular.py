"""
Python wrapper for nebular
"""

import numpy as np
import time
import os


def nebular(temperature, density, wave, file=None, fractions=None, output=None,
            he_a=None, case=None, fwhm=None, no_head=False, format=0, verbose=False):
    """
      PURPOSE: Calculates the nebular spectrum for a mixed hydrogen helium gas in
               ionization equilibrium, including bound-free, free-free, two-photon
               and line emission.
               Calculations are done for a user-specified wavelength / frequency
               range including step size, or on a pre-defined grid.
               The input can be in wavelengths (Angstrom) or in frequencies (Hz).
               Wavelengths are assumed if numeric values for the range/grid are <1e7.
               The output spectrum will be scaled in j_lambda or j_nu, depending on
               whether wavelenghts or frequencies are given.
               Alternatively, the atomic values for gamma (or nu*gamma) can be returned.

      OPTIONS (mandatory):
               -r range_min range_max range_delta (Angstrom or Hz)    --OR--
               -i input wavelength/frequency table (ASCII)

               -t electron temperature [K]
               -n electron number density [cm-3]

      OPTIONS (optional):
              [-f H+ He+ He++ ionization fractions (0...1); calculated internally if omitted]
              [-o output file name (default: 'nebular_spectrum.dat')]
              [-a Helium abundance ratio by parts (default: 0.10)]
              [-k (omits emission line spectrum; for faster calculations of the continuum)]
              [-c A or B (Case A or Case B for the emission lines; default: B)
              [-w FWHM (Convolve total spectrum with a Gaussian of this FWHM [Angstrom or Hz]) ]
              [-b (Suppress header line in output file)]
              [-u format (0, 1 or 2; default: 0); selects output units]
                  0: outputs j = 1/(4 pi) N_X N_e gamma
                  1: outputs gamma (provides access to the atomic data tables)
                  2: outputs nu*gamma (for convencience)

    """
    dire = "/home/star2/jvhs1/python/nebular-master/src/"
    arg = "-t "+str(temperature)+" -n "+str(density)

    if type(wave) == str:
        arg += "-i "+wave
    else:
        arg += " -r "+str(wave[0])+" "+str(wave[-1])+" "+str(wave[2]-wave[1])
    if he_a != None: arg +=" -a "+str(he_a)
    if fwhm != None: arg +=" -w "+str(fwhm)
    arg +=" -u "+str(format)
    if output != None:
        arg +=" -o "+str(output)
    else:
        output = "nebular_spectrum.dat"

    if verbose: print(dire+"nebular "+arg)
    os.system(dire+"nebular "+arg)

    data = np.loadtxt(output,dtype ={'names': ('freq', 'wave', 'flux'),'formats': ('f8', 'f8', 'f8')} )
    time.sleep(2)
    return data

def help():
    dire = "/home/star2/jvhs1/python/nebular-master/src/"
    os.system(dire+"nebular")
