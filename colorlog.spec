#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colorlog
Version  : 6.6.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/8e/8f/1537ebed273d43edd3bb21f1e5861549b7cfcb1d47523d7277cab988cec2/colorlog-6.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/8f/1537ebed273d43edd3bb21f1e5861549b7cfcb1d47523d7277cab988cec2/colorlog-6.6.0.tar.gz
Summary  : Add colours to the output of Python's logging module.
Group    : Development/Tools
License  : MIT
Requires: colorlog-license = %{version}-%{release}
Requires: colorlog-python = %{version}-%{release}
Requires: colorlog-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(black)
BuildRequires : pypi(colorama)
BuildRequires : pypi(flake8)
BuildRequires : pypi(mypy)
BuildRequires : pypi(setuptools)
BuildRequires : pypi(types_colorama)

%description
===========================

%package license
Summary: license components for the colorlog package.
Group: Default

%description license
license components for the colorlog package.


%package python
Summary: python components for the colorlog package.
Group: Default
Requires: colorlog-python3 = %{version}-%{release}

%description python
python components for the colorlog package.


%package python3
Summary: python3 components for the colorlog package.
Group: Default
Requires: python3-core
Provides: pypi(colorlog)
Requires: pypi(black)
Requires: pypi(colorama)
Requires: pypi(flake8)
Requires: pypi(mypy)
Requires: pypi(types_colorama)

%description python3
python3 components for the colorlog package.


%prep
%setup -q -n colorlog-6.6.0
cd %{_builddir}/colorlog-6.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1637357521
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/colorlog
cp %{_builddir}/colorlog-6.6.0/LICENSE %{buildroot}/usr/share/package-licenses/colorlog/5d70b54581cc4a1ab2ee60f7bea991a2d56340a5
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/colorlog/5d70b54581cc4a1ab2ee60f7bea991a2d56340a5

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
