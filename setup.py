import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='myshowsapi',
      version='0.1.4',
      description='API wrapper for http://api.myshows.me/',
      long_description=read('README.rst'),
      url='http://github.com/kreedz/myshowsapi',
      author='Artur Tukaev',
      license='MIT',
      packages=['myshowsapi'],
      install_requires=['requests'],
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
      ],
      keywords='myshows.me myshows api')
