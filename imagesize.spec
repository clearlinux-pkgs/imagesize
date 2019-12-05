#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imagesize
Version  : 1.1.0
Release  : 41
URL      : https://files.pythonhosted.org/packages/41/f5/3cf63735d54aa9974e544aa25858d8f9670ac5b4da51020bbfc6aaade741/imagesize-1.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/41/f5/3cf63735d54aa9974e544aa25858d8f9670ac5b4da51020bbfc6aaade741/imagesize-1.1.0.tar.gz
Summary  : Getting image size from png/jpeg/jpeg2000/gif file
Group    : Development/Tools
License  : MIT
Requires: imagesize-license = %{version}-%{release}
Requires: imagesize-python = %{version}-%{release}
Requires: imagesize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
It parses image files' header and return image size.
        
        * PNG
        * JPEG
        * JPEG2000
        * GIF
        * TIFF (experimental)
        
        This is a pure Python library.

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
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571089985
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
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
cp %{_builddir}/imagesize-1.1.0/LICENSE.rst %{buildroot}/usr/share/package-licenses/imagesize/e2d81b7a944986d62b6fed34a9aa38877eba7a7e
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
