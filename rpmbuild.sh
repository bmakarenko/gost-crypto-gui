#!/bin/bash
rm -f gostcryptogui/*.pyc
mkdir -p ~/rpmbuild/SPEC ~/rpmbuild/SOURCES
tar -czf ~/rpmbuild/SOURCES/gostcryptogui.tar.gz gostcryptogui
cp gostcryptogui.spec ~/rpmbuild/SPEC/
cp gost-crypto-gui.png ~/rpmbuild/SOURCES/
cp gost-crypto-gui.py ~/rpmbuild/SOURCES/
cp gost-crypto-gui.desktop ~/rpmbuild/SOURCES/
cp x-extension-enc.xml ~/rpmbuild/SOURCES/
cp x-extension-sig.xml ~/rpmbuild/SOURCES/
cp x-extension-sgn.xml ~/rpmbuild/SOURCES/
cp encrypted.png ~/rpmbuild/SOURCES/
cp signed.png ~/rpmbuild/SOURCES/
cp emblem-nochain.png ~/rpmbuild/SOURCES/
cp emblem-unverified.png ~/rpmbuild/SOURCES/
cp emblem-verified.png ~/rpmbuild/SOURCES/
cp setup.py ~/rpmbuild/SOURCES/
rpmbuild -ba --target i386  ~/rpmbuild/SPEC/gostcryptogui.spec
rpmbuild -ba --target x86_64  ~/rpmbuild/SPEC/gostcryptogui.spec

cp nautilus/gost-crypto-gui-menu.py ~/rpmbuild/SOURCES/
cp nautilus/gost-crypto-gui-emblem.py ~/rpmbuild/SOURCES/
cp nautilus-gostcryptogui.spec ~/rpmbuild/SPEC/
rpmbuild -ba --target i386 ~/rpmbuild/SPEC/nautilus-gostcryptogui.spec
rpmbuild -ba --target x86_64 ~/rpmbuild/SPEC/nautilus-gostcryptogui.spec

cp caja/gost-crypto-gui-menu.py ~/rpmbuild/SOURCES/
cp caja/gost-crypto-gui-emblem.py ~/rpmbuild/SOURCES/
cp caja-gostcryptogui.spec ~/rpmbuild/SPEC/
rpmbuild -ba --target i386 ~/rpmbuild/SPEC/caja-gostcryptogui.spec
rpmbuild -ba --target x86_64 ~/rpmbuild/SPEC/caja-gostcryptogui.spec

cp nemo/gost-crypto-gui-menu.py ~/rpmbuild/SOURCES/
cp nemo/gost-crypto-gui-emblem.py ~/rpmbuild/SOURCES/
cp nemo-gostcryptogui.spec ~/rpmbuild/SPEC/
rpmbuild -ba --target i386 ~/rpmbuild/SPEC/nemo-gostcryptogui.spec
rpmbuild -ba --target x86_64 ~/rpmbuild/SPEC/nemo-gostcryptogui.spec