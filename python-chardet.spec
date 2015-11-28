%define		module	chardet

Summary:	Character encoding auto-detection in Python
Summary(pl.UTF-8):	Automatyczne wykrywanie kodowania znaków w Pythonie
Name:		python-%{module}
Version:	2.3.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/c/chardet/%{module}-%{version}.tar.gz
# Source0-md5:	25274d664ccb5130adae08047416e1a8
URL:		https://pypi.python.org/pypi/chardet
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Character encoding auto-detection in Python. As smart as your browser.

%description -l pl.UTF-8
Automatyczne wykrywanie kodowania znaków w Pythonie. Tak zmyślne jak w
przeglądarce.

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/chardetect
%doc README.rst
%dir %{py_sitescriptdir}/chardet
%{py_sitescriptdir}/chardet/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
