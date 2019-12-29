#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tets

%define		module	chardet
Summary:	Character encoding auto-detection in Python 2
Summary(pl.UTF-8):	Automatyczne wykrywanie kodowania znaków w Pythonie 2
Name:		python-%{module}
Version:	3.0.4
Release:	3
License:	LGPL v2.1+
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/chardet/
Source0:	https://files.pythonhosted.org/packages/source/c/chardet/%{module}-%{version}.tar.gz
# Source0-md5:	7dd1ba7f9c77e32351b0a0cfacf4055c
URL:		https://pypi.org/project/chardet/
%if %{with python2}
BuildRequires:	python >= 1:2.6
BuildRequires:	python-devel >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-hypothesis
BuildRequires:	python-pytest
%endif
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-devel >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis
BuildRequires:	python3-pytest
%endif
%endif
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
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
Requires:	python3-modules >= 1:3.3

%description -n python3-chardet
Character encoding auto-detection in Python. As smart as your browser.

%description -n python3-chardet -l pl.UTF-8
Automatyczne wykrywanie kodowania znaków w Pythonie. Tak zmyślne jak w
przeglądarce.

%package apidocs
Summary:	API documentation for Python chardet module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona chardet
Group:		Documentation

%description apidocs
API documentation for Python chardet module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona chardet.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} -m pytest test.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} -m pytest test.py
%endif
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
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

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,api,*.html,*.js}
%endif
