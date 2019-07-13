#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imagesize
Version  : 1.1.0
Release  : 38
URL      : https://files.pythonhosted.org/packages/41/f5/3cf63735d54aa9974e544aa25858d8f9670ac5b4da51020bbfc6aaade741/imagesize-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/f5/3cf63735d54aa9974e544aa25858d8f9670ac5b4da51020bbfc6aaade741/imagesize-1.1.0.tar.gz
Summary  : Getting image size from png/jpeg/jpeg2000/gif file
Group    : Development/Tools
License  : MIT
Requires: imagesize-license = %{version}-%{release}
Requires: imagesize-python = %{version}-%{release}
Requires: imagesize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : setuptools-legacypython

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

%description python3
python3 components for the imagesize package.


%prep
%setup -q -n imagesize-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554320981
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imagesize
cp LICENSE.rst %{buildroot}/usr/share/package-licenses/imagesize/LICENSE.rst
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/imagesize/LICENSE.rst

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
