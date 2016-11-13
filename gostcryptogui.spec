%define name gostcryptogui
%define version 0.2
%define unmangled_version 0.2
%define unmangled_version 0.2
%define release 1

Summary: A PyQt GUI for performing cryptographic operations over files using GOST algorithms
Name: %{name}
Version: %{version}
Release: %{release}
Source0: gostcryptogui.tar.gz
Source1: setup.py
Source2: gost-crypto-gui.py
Source3: gost-crypto-gui-menu.py
Source4: gost-crypto-gui.png
Source5: gost-crypto-gui.desktop
Source6: x-extension-enc.xml
Source7: x-extension-sig.xml
Source8: encrypted.png
Source9: signed.png
Source10: emblem-nochain.png
Source11: emblem-unverified.png
Source12: emblem-verified.png
Source13: gost-crypto-gui-emblem.py
License: MIT
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: x86_64
Vendor: Boris Makarenko <bmakarenko90@gmail.com>
Url: http://github.com/bmakarenko/gost-crypto-gui
Requires: PyQt4, nautilus-python, lsb-cprocsp-capilite-64, python-setuptools

%description
A PyQt GUI for performing cryptographic operations over files using GOST algorithms

%prep
tar -zxf %{SOURCE0}

%build
python %{SOURCE1} build

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_libdir}/nautilus/extensions-2.0/python
mkdir -p %{buildroot}/%{_datadir}/pixmaps
mkdir -p %{buildroot}/%{_datadir}/icons
mkdir -p %{buildroot}/%{_datadir}/applications
mkdir -p %{buildroot}/%{_datadir}/mime/applications
%{__install} -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/gost-crypto-gui.py
%{__install} -m 0755 %{SOURCE3} %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/gost-crypto-gui-menu.py
%{__install} -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/gost-crypto-gui.png
%{__install} -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/applications/gost-crypto-gui.desktop
%{__install} -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/mime/applications/x-extension-enc.xml
%{__install} -m 0644 %{SOURCE7} %{buildroot}%{_datadir}/mime/applications/x-extension-sig.xml
%{__install} -m 0644 %{SOURCE8} %{buildroot}%{_datadir}/icons/encrypted.png
%{__install} -m 0644 %{SOURCE9} %{buildroot}%{_datadir}/icons/signed.png
%{__install} -m 0644 %{SOURCE10} %{buildroot}%{_datadir}/icons/emblem-nochain.png
%{__install} -m 0644 %{SOURCE11} %{buildroot}%{_datadir}/icons/emblem-unverified.png
%{__install} -m 0644 %{SOURCE12} %{buildroot}%{_datadir}/icons/emblem-verified.png
%{__install} -m 0755 %{SOURCE13} %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/gost-crypto-gui-emblem.py
python %{SOURCE1} install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%post
xdg-mime install %{_datadir}/mime/applications/x-extension-enc.xml
xdg-mime install %{_datadir}/mime/applications/x-extension-sig.xml
xdg-desktop-menu install --mode system %{_datadir}/applications/gost-crypto-gui.desktop
xdg-icon-resource install --context mimetypes --mode system --size 256 %{_datadir}/icons/encrypted.png application-x-extension-enc
xdg-icon-resource install --context mimetypes --mode system --size 256 %{_datadir}/icons/signed.png application-x-extension-sig
xdg-icon-resource install --size 24 --context emblems %{_datadir}/icons/emblem-nochain.png
xdg-icon-resource install --size 24 --context emblems %{_datadir}/icons/emblem-unverified.png
xdg-icon-resource install --size 24 --context emblems %{_datadir}/icons/emblem-verified.png
xdg-icon-resource forceupdate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{_bindir}/gost-crypto-gui.py
%{_libdir}/nautilus/extensions-2.0/python/gost-crypto-gui-menu.py
%{_libdir}/nautilus/extensions-2.0/python/gost-crypto-gui-emblem.py
%{_datadir}/pixmaps/gost-crypto-gui.png
%{_datadir}/applications/gost-crypto-gui.desktop
%{_datadir}/mime/applications/x-extension-enc.xml
%{_datadir}/mime/applications/x-extension-sig.xml
%{_datadir}/icons/encrypted.png
%{_datadir}/icons/signed.png
%{_datadir}/icons/emblem-nochain.png
%{_datadir}/icons/emblem-unverified.png
%{_datadir}/icons/emblem-verified.png

%changelog
* Sun Nov 13 2016 Boris Makarenko <bmakarenko90@gmail.com> - 0.2-1
- Release 0.2
- Adding emblems on signature files

* Tue Oct 25 2016 Boris Makarenko <bmakarenko90@gmail.com> - 0.1-1
- Initial build
