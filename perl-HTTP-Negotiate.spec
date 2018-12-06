#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Negotiate
Version  : 6.01
Release  : 24
URL      : https://cpan.metacpan.org/authors/id/G/GA/GAAS/HTTP-Negotiate-6.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GAAS/HTTP-Negotiate-6.01.tar.gz
Summary  : choose a variant to serve
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(HTTP::Headers)
BuildRequires : perl(HTTP::Request)
BuildRequires : perl(URI)

%description
NAME
HTTP::Negotiate - choose a variant to serve
SYNOPSIS
use HTTP::Negotiate qw(choose);

%package dev
Summary: dev components for the perl-HTTP-Negotiate package.
Group: Development
Provides: perl-HTTP-Negotiate-devel = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Negotiate package.


%prep
%setup -q -n HTTP-Negotiate-6.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/HTTP/Negotiate.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Negotiate.3
