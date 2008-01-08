#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Strict
Summary:	Test::Strict - Check syntax, presence of use strict; and test coverage
#Summary(pl):	
Name:		perl-Test-Strict
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/S/SM/SMUELLER/Test-Strict-0.08.tar.gz
# Source0-md5:	8eccccf18d453b6e5453c07c7c6beed4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Devel::Cover) >= 0.43
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The most basic test one can write is "does it compile ?".
This module tests if the code compiles and play nice with Test::Simple modules.

Another good practice this module can test is to "use strict;" in all perl files.

By setting a minimum test coverage through all_cover_ok(), a code author
can ensure his code is tested above a preset level of kwality throughout the development cycle.

Along with Test::Pod, this module can provide the first tests to setup for a module author.

This module should be able to run under the -T flag for perl >= 5.6.
All paths are untainted with the following pattern: qr|^([-+@\w./:\\]+)$|
controlled by $Test::Strict::UNTAINT_PATTERN.


# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
#%%{perl_vendorlib}/Test/Strict
%{_mandir}/man3/*
