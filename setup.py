from os import listdir
from setuptools import setup, find_packages

setup(
    name='askocli',
    version='0.3.4',
    description='Command line interface for a distant AskOmics',
    author='Xavier Garnier',
    author_email='xavier.garnier@irisa.fr',
    url='https://github.com/askomics/askocli',
    download_url='https://github.com/askomics/askocli/archive/0.3.4.git tar.gz',
    install_requires=['requests>=2.4.3'],
    packages=find_packages(),
    license='AGPL',
    platforms='Posix; MacOS X; Windows',
    scripts=['bin/' + f for f in listdir('bin')],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ])
