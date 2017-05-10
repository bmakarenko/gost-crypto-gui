gost-crypto-gui
===============
A PyQt GUI for performing cryptographic operations over files using GOST algorithms

Allows user to perform cryptographic operations over files, including directly from the Nautilus file manager.
Five operations are supported: sign, verify signature, dettach signature, encrypt and decrypt.
Resulting files are PKCS#7 compilant and compatible with other similar software.

gost-crypto-gui was was designed for the GosLinux distribution by The Federal Bailiffs' Service of Russia and uses just few features of CryptoPro CSP. Feel free to suggest new features.

# Usage
There are three ways you may use this software.
- From command line: type python /usr/bin/gost-crypto-gui.py --help to get more info;
- From context menu item(s) in Nautilus 2 or Caja(el7 branch);
- From the main window of the application.

# Building RPM package
You can use SPEC file located in this repository. For easier building an RPM package of this software you may run rpmbuild.sh shell-script. Make sure you have installed rpmbuild utility and python-setuptools package. Then you can run <b>rpmbuild.sh</b> shell-script to build RPM package. The package you can find at <your home directory>/rpmbuild/RPMS

Example
```
# yum install rpm-build python-setuptools
$ git clone https://github.com/bmakarenko/gost-crypto-gui.git
$ cd gost-crypto-gui/
$ ./rpmbuild.sh
# rpm -ihv ~/rpmbuild/RPMS/i386/gostcryptogui-0.2-1.i386.rpm
```
