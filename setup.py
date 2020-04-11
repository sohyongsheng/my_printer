from pathlib import Path

import setuptools

with Path('README.md').open() as f:
    long_description = f.read()

setuptools.setup(
    name = 'sohyongsheng-example-pkg',
    version = '0.01',
    author = 'Soh Yong Sheng',
    author_email = 'sohyongsheng@gmail.com',
    description = 'My printer.'
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 


