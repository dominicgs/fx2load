import os
from setuptools import setup, find_packages

setup(
    name='pyFXload',
    version='0.0',
    url='',
    license='GPL2',
    entry_points={
        'console_scripts': [
            'fx2load = fx2.fx2load:main',
        ],
    },
    author='Dominic Spill',
    author_email='dominicgs@gmail.com',
    tests_require=[''],
    install_requires=['pyusb'],
    description='Python version of fx2load',
    #long_description=read('../README.md'),
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GPL2 License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        ],
    extras_require={}
)
