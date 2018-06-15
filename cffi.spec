#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cffi
Version  : 1.11.5
Release  : 62
URL      : http://pypi.debian.net/cffi/cffi-1.11.5.tar.gz
Source0  : http://pypi.debian.net/cffi/cffi-1.11.5.tar.gz
Summary  : Foreign Function Interface for Python calling C code.
Group    : Development/Tools
License  : MIT
Requires: cffi-python3
Requires: cffi-python
Requires: pycparser
BuildRequires : cffi
BuildRequires : libffi-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libffi)
BuildRequires : pycparser

BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : setuptools-legacypython

%description
CFFI
        ====
        
        Foreign Function Interface for Python calling C code.

%package legacypython
Summary: legacypython components for the cffi package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the cffi package.


%package python
Summary: python components for the cffi package.
Group: Default
Requires: cffi-python3

%description python
python components for the cffi package.


%package python3
Summary: python3 components for the cffi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cffi package.


%prep
%setup -q -n cffi-1.11.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1528556437
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1528556437
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
