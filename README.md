gost-crypto-gui
===============
A PyQt GUI for performing cryptographic operations over files using GOST algorithms

Allows user to perform cryptographic operations over files, including directly from the Nautilus file manager.
Five operations are supported: sign, verify signature, dettach signature, encrypt and decrypt.
Resulting files are PKCS#7 compilant and compatible with other similar software.

gost-crypto-gui was was designed for the GosLinux distribution by The Federal Bailiffs' Service of Russia and uses just few features of CryptoPro CSP.

# Usage
There are three ways to use this software.
From command line: type python /usr/bin/gost-crypto-gui.py --help to get more info.
From context menu in Nautilus 2
From main window of the application

# Building RPM package
Make sure you have installed rpmbuild utility and python-setuptools package. Then you can run <b>rpmbuild.sh</b> shell-script to build RPM package. The package you can find at <your home directory>/rpmbuild/RPMS
