import setuptools

# upload to pip
# pip install .
# python3 setup.py sdist bdist_wheel
# twine upload dist/pydoppler-0.1.8.tar.gz

import os



setuptools.setup(
     name='nebularpy',
     version='0.1.0',
     packages=['nebularpy'] ,
     author="Juan V. Hernandez Santisteban",
     author_email="jvhs1@st-andrews.ac.uk",
     description="A python wrapper for Mischa Schirmer Nebular sowftare",
   long_description_content_type="text/markdown",
     url="https://github.com/alymantara/nebularpy",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
         ],
 )
