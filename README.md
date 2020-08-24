# NebularPy

  This is the repository for a python wrapper for Mischa Schirmer's NEBULAR software.

 ## Requirements & Installation

  You require to download and install NEBULAR from https://github.com/mischaschirmer/nebular .


  ```
  python setup.py install
  ```
 ##  Section 1:  Parameters

 ##  Section 2:  Usage

```python
import nebular
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2000,25000,1.)
model = nebular.nebular(10000,20,x)
```
Now, plotting the output
```python
fig = plt.figure(figsize=(12,6))

plt.plot(model['wave'],model['flux'],color='b')

plt.yscale('log')
plt.xlim(2000,25000)
plt.xlabel(r"Wavlength / $\AA$")
plt.ylabel(r"Flux / erg s$^{-1}$ cm$^{-2}$ $\AA^{-1}$")
plt.tight_layout()
```
  <p align="middle">
     <img src="nebular_test.png"  height="450" />
  </p>
