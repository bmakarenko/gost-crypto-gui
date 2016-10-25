%define name gostcryptogui
%define version 0.1
%define unmangled_version 0.1
%define unmangled_version 0.1
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
Source6: enc-mime.xml
Source7: sig-mime.xml
Source8: encrypted.png
Source9: signed.png
License: MIT
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
BuildArch: i686
Vendor: Boris Makarenko <bmakarenko90@gmail.com>
Url: http://github.com/bmakarenko/gost-crypto-gui
Requires: PyQt4, nautilus-python, lsb-cprocsp-capilite

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
%{__install} -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/gost-crypto-gui.py
%{__install} -m 0755 %{SOURCE3} %{buildroot}%{_libdir}/nautilus/extensions-2.0/python/gost-crypto-gui-menu.py
%{__install} -m 0644 %{SOURCE4} %{buildroot}%{_datadir}/pixmaps/gost-crypto-gui.png
%{__install} -m 0644 %{SOURCE5} %{buildroot}%{_datadir}/applications/gost-crypto-gui.desktop
python %{SOURCE1} install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%post
xdg-mime install %{SOURCE6}
xdg-mime install %{SOURCE7}
xdg-icon-resource install --context mimetypes --mode system --size 256 %{SOURCE8} application-x-extension-enc
xdg-icon-resource install --context mimetypes --mode system --size 256 %{SOURCE9} application-x-extension-sig
xdg-icon-resource forceupdate

%clean
rm -rf $RPM_BUILD_ROOT

%files -f INSTALLED_FILES
%defattr(-,root,root)
%{_bindir}/gost-crypto-gui.py
%{_libdir}/nautilus/extensions-2.0/python/gost-crypto-gui-menu.py
%{_datadir}/pixmaps/gost-crypto-gui.png
%{_datadir}/applications/gost-crypto-gui.desktop

%changelog
* Tue Oct 25 2016 Boris Makarenko <bmakarenko90@gmail.com>
- Initial build