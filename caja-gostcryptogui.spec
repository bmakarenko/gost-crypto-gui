%define name caja-gostcryptogui
%define version 0.2
%define unmangled_version 0.2
%define unmangled_version 0.2
%define release 1

Summary: Caja plugins for gost-crypto-gui
Name: %{name}
Version: %{version}
Release: %{release}
Source0: gost-crypto-gui-menu.py
Source1: gost-crypto-gui-emblem.py

License: MIT
Group: System Environment/Base
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Prefix: %{_prefix}
Vendor: Boris Makarenko <bmakarenko90@gmail.com>
Url: http://github.com/bmakarenko/gost-crypto-gui
BuildArch: noarch

Requires: gostcryptogui
Requires: python-caja

%description
Caja plugins for gost-crypto-gui

%install
mkdir -p %{buildroot}/%{_datadir}/caja-python/extensions
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{_datadir}/caja-python/extensions/gost-crypto-gui-menu.py
%{__install} -m 0755 %{SOURCE1} %{buildroot}%{_datadir}/caja-python/extensions/gost-crypto-gui-emblem.py
python -m py_compile %{buildroot}%{_datadir}/caja-python/extensions/gost-crypto-gui-menu.py
python -m py_compile %{buildroot}%{_datadir}/caja-python/extensions/gost-crypto-gui-emblem.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/caja-python/extensions/*.py
%{_datadir}/caja-python/extensions/*.pyc


%changelog
* Fri Sep 12 2019 Boris Makarenko <bmakarenko90@gmail.com> - 0.2-1
- Exclude dettach menu item if there is an original file

* Mon May 22 2017 Boris Makarenko <bmakarenko90@gmail.com> - 0.1-1
- Derived from main package
