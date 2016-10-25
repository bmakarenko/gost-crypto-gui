from setuptools import setup

setup(name='gostcryptogui',
      version='0.1',
      description='A PyQt GUI for performing cryptographic operations over files using GOST algorithms',
      url='http://github.com/bmakarenko/gost-crypto-gui',
      author='Boris Makarenko',
      author_email='bmakarenko90@gmail.com',
      license='MIT',
      packages=['gostcryptogui'],
      zip_safe=False, install_requires=['PyQt4'])
