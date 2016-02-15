#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cffi
Version  : 1.3.1
Release  : 28
URL      : https://pypi.python.org/packages/source/c/cffi/cffi-1.3.1.tar.gz
Source0  : https://pypi.python.org/packages/source/c/cffi/cffi-1.3.1.tar.gz
Summary  : Foreign Function Interface for Python calling C code.
Group    : Development/Tools
License  : MIT
Requires: cffi-python
BuildRequires : cffi
BuildRequires : libffi-dev
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pkgconfig(libffi)
BuildRequires : pycparser
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
No detailed description available

%package python
Summary: python components for the cffi package.
Group: Default

%description python
python components for the cffi package.


%prep
%setup -q -n cffi-1.3.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python setup_base.py build_ext -f -i ; python3 setup_base.py build_ext -f -i ; PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages py.test --verbose
%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
