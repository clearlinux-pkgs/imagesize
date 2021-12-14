#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imagesize
Version  : 1.3.0
Release  : 62
URL      : https://files.pythonhosted.org/packages/f6/27/b147794d43249e8303a06f427e407a090696b65b81045e36f8873d8d8a42/imagesize-1.3.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f6/27/b147794d43249e8303a06f427e407a090696b65b81045e36f8873d8d8a42/imagesize-1.3.0.tar.gz
Summary  : Getting image size from png/jpeg/jpeg2000/gif file
Group    : Development/Tools
License  : MIT
Requires: imagesize-license = %{version}-%{release}
Requires: imagesize-python = %{version}-%{release}
Requires: imagesize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
imagesize
=============
.. image:: https://travis-ci.org/shibukawa/imagesize_py.svg?branch=master
:target: https://travis-ci.org/shibukawa/imagesize_py

%package license
Summary: license components for the imagesize package.
Group: Default

%description license
license components for the imagesize package.


%package python
Summary: python components for the imagesize package.
Group: Default
Requires: imagesize-python3 = %{version}-%{release}

%description python
python components for the imagesize package.


%package python3
Summary: python3 components for the imagesize package.
Group: Default
Requires: python3-core
Provides: pypi(imagesize)

%description python3
python3 components for the imagesize package.


%prep
%setup -q -n imagesize-1.3.0
cd %{_builddir}/imagesize-1.3.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1636488382
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
mkdir -p %{buildroot}/usr/share/package-licenses/imagesize
cp %{_builddir}/imagesize-1.3.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/imagesize/e2d81b7a944986d62b6fed34a9aa38877eba7a7e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/imagesize/e2d81b7a944986d62b6fed34a9aa38877eba7a7e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
