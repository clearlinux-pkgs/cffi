#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cffi
Version  : 1.14.5
Release  : 100
URL      : https://files.pythonhosted.org/packages/a8/20/025f59f929bbcaa579704f443a438135918484fffaacfaddba776b374563/cffi-1.14.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/20/025f59f929bbcaa579704f443a438135918484fffaacfaddba776b374563/cffi-1.14.5.tar.gz
Summary  : Foreign Function Interface for Python calling C code.
Group    : Development/Tools
License  : MIT
Requires: cffi-license = %{version}-%{release}
Requires: cffi-python = %{version}-%{release}
Requires: cffi-python3 = %{version}-%{release}
Requires: pycparser
BuildRequires : buildreq-distutils3
BuildRequires : cffi
BuildRequires : libffi-dev
BuildRequires : pkgconfig(libffi)
BuildRequires : pycparser

%description
CFFI
        ====
        
        Foreign Function Interface for Python calling C code.

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
Provides: pypi(cffi)
Requires: pypi(pycparser)

%description python3
python3 components for the cffi package.


%prep
%setup -q -n cffi-1.14.5
cd %{_builddir}/cffi-1.14.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613143043
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/cffi
cp %{_builddir}/cffi-1.14.5/LICENSE %{buildroot}/usr/share/package-licenses/cffi/65e8b9015ffb0747c23370a3d3af2a796c64780e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/cffi/65e8b9015ffb0747c23370a3d3af2a796c64780e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
