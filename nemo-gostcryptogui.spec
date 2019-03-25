%define name nemo-gostcryptogui
%define version 0.1
%define unmangled_version 0.1
%define unmangled_version 0.1
%define release 1

Summary: Nemo plugins for gost-crypto-gui
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
Requires: python-nemo

%description
Nemo plugins for gost-crypto-gui

%install
mkdir -p %{buildroot}/%{_datadir}/nemo-python/extensions
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{_datadir}/nemo-python/extensions/gost-crypto-gui-menu.py
%{__install} -m 0755 %{SOURCE1} %{buildroot}%{_datadir}/nemo-python/extensions/gost-crypto-gui-emblem.py
python -m py_compile %{buildroot}%{_datadir}/nemo-python/extensions/gost-crypto-gui-menu.py
python -m py_compile %{buildroot}%{_datadir}/nemo-python/extensions/gost-crypto-gui-emblem.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/nemo-python/extensions/*.py
%{_datadir}/nemo-python/extensions/*.pyc


%changelog
* Mon Mar 25 2019 Boris Makarenko <bmakarenko90@gmail.com> - 0.1-1
- Derived from main package
