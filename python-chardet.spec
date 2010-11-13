%define		module	chardet

Summary:	Character encoding auto-detection in Python
Summary(pl.UTF-8):	Automatyczne wykrywanie kodowania znaków w Pythonie
Name:		python-%{module}
Version:	1.0.1
Release:	6
License:	LGPL
Group:		Libraries/Python
Source0:	http://chardet.feedparser.org/download/%{module}-%{version}.tgz
# Source0-md5:	f8c510a6fac300fe0ac9a0c24a76a7ba
URL:		http://chardet.feedparser.org/
BuildRequires:	python >= 1:2.4
BuildRequires:	python-devel >= 1:2.4
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Character encoding auto-detection in Python. As smart as your browser.

%description -l pl.UTF-8
Automatyczne wykrywanie kodowania znaków w Pythonie. Tak zmyślne jak w
przeglądarce.

%prep
%setup -q -n %{module}-%{version}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%dir %{py_sitescriptdir}/chardet
%{py_sitescriptdir}/chardet/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/*.egg-info
%endif
