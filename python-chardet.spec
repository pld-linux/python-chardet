#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module

%define		module	chardet
Summary:	Character encoding auto-detection in Python 2
Summary(pl.UTF-8):	Automatyczne wykrywanie kodowania znaków w Pythonie 2
Name:		python-%{module}
Version:	2.3.0
Release:	3
License:	LGPL v2.1+
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/chardet/%{module}-%{version}.tar.gz
# Source0-md5:	25274d664ccb5130adae08047416e1a8
URL:		https://pypi.python.org/pypi/chardet
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.2
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Character encoding auto-detection in Python. As smart as your browser.

%description -l pl.UTF-8
Automatyczne wykrywanie kodowania znaków w Pythonie. Tak zmyślne jak w
przeglądarce.

%package -n python3-chardet
Summary:	Character encoding auto-detection in Python 3
Summary(pl.UTF-8):	Automatyczne wykrywanie kodowania znaków w Pythonie 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-chardet
Character encoding auto-detection in Python. As smart as your browser.

%description -n python3-chardet -l pl.UTF-8
Automatyczne wykrywanie kodowania znaków w Pythonie. Tak zmyślne jak w
przeglądarce.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python3}
%py3_install
%endif

%if %{with python2}
%py_install

%py_postclean
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%attr(755,root,root) %{_bindir}/chardetect
%{py_sitescriptdir}/chardet
%{py_sitescriptdir}/chardet-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-chardet
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/chardet
%{py3_sitescriptdir}/chardet-%{version}-py*.egg-info
%endif
