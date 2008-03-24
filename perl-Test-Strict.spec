#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	Strict
Summary:	Test::Strict - Check syntax, presence of use strict; and test coverage
Summary(pl.UTF-8):	Test::Strict - sprawdzanie składni, obecności "use strict" i pokrycia testami
Name:		perl-Test-Strict
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8eccccf18d453b6e5453c07c7c6beed4
URL:		http://search.cpan.org/dist/Test-Strict/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Cover >= 0.43
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The most basic test one can write is "does it compile?". This module
tests if the code compiles and play nice with Test::Simple modules.

Another good practice this module can test is to "use strict;" in all
perl files.

By setting a minimum test coverage through all_cover_ok(), a code
author can ensure his code is tested above a preset level of quality
throughout the development cycle.

Along with Test::Pod, this module can provide the first tests to setup
for a module author.

%description -l pl.UTF-8
Najbardziej podstawowym testem, który można napisać, to "czy to się
kompiluje?". Ten moduł sprawdza więc, czy kod się kompiluje i dobrze
współpracuje z modułami Test::Simple.

Inną dobrą praktyką, jaką może testować ten moduł, to czy wszystkie
pliki perlowe zawierają "use strict;".

Ustawiając minimalne pokrycie testami poprzez all_cover_ok(), autor
kodu może upewnić się, że jego kod jest testowany pod kątem
określonego poziomu jakości.

Wraz z Test::Pod ten moduł może zapewnić autorom modułów pierwsze
testy.

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
%{_mandir}/man3/*
