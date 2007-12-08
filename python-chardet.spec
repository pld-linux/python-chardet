%define		module	chardet

Summary:	Character encoding auto-detection in Python
Summary(pl.UTF-8):	Automatyczne wykrywanie kodowania znaków w Pythonie
Name:		python-%{module}
Version:	1.0
Release:	1
License:	LGPL
Group:		Libraries/Python
Source0:	http://chardet.feedparser.org/download/%{module}-%{version}.tgz
# Source0-md5:	29f69d097052a4eae3774382c234cf2b
URL:		http://chardet.feedparser.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
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
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
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
%{py_sitescriptdir}/*.egg-info
