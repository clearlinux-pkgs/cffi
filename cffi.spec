#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cffi
Version  : 1.12.2
Release  : 74
URL      : https://files.pythonhosted.org/packages/64/7c/27367b38e6cc3e1f49f193deb761fe75cda9f95da37b67b422e62281fcac/cffi-1.12.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/64/7c/27367b38e6cc3e1f49f193deb761fe75cda9f95da37b67b422e62281fcac/cffi-1.12.2.tar.gz
Summary  : Foreign Function Interface for Python calling C code.
Group    : Development/Tools
License  : MIT
Requires: cffi-license = %{version}-%{release}
Requires: cffi-python = %{version}-%{release}
Requires: cffi-python3 = %{version}-%{release}
Requires: pycparser
BuildRequires : buildreq-distutils23
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : libffi-dev
BuildRequires : pkgconfig(libffi)
BuildRequires : pycparser
BuildRequires : python-dev
BuildRequires : setuptools-legacypython

%description
CFFI
====
Foreign Function Interface for Python calling C code.
Please see the [Documentation](http://cffi.readthedocs.org/) or uncompiled
in the doc/ subdirectory.

%package legacypython
Summary: legacypython components for the cffi package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the cffi package.


%package license
Summary: license components for the cffi package.
Group: Default

%description license
license components for the cffi package.


%package python
Summary: python components for the cffi package.
Group: Default
Requires: cffi-python3 = %{version}-%{release}

%description python
python components for the cffi package.


%package python3
Summary: python3 components for the cffi package.
Group: Default
Requires: python3-core

%description python3
python3 components for the cffi package.


%prep
%setup -q -n cffi-1.12.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551309699
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1551309699
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cffi
cp LICENSE %{buildroot}/usr/share/package-licenses/cffi/LICENSE
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cffi/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
