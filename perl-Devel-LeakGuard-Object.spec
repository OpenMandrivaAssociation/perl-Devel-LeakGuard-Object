%define upstream_name    Devel-LeakGuard-Object
%define upstream_version 0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    4

Summary:    Scoped object leak checking
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(List::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(Test::Differences)
BuildRequires: perl(Test::More)
BuildRequires: perl(latest)
BuildRequires: perl(Module::Build)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides tracking of objects, for the purpose of detecting
memory leaks due to circular references or innappropriate caching schemes.

It is derived from, and backwards compatible with Adam Kennedy's the
Devel::Leak::Object manpage. Any errors are mine.

It works by overridding 'bless' and adding a synthetic 'DESTROY' method to
any tracked classes so that it can maintain a count of blessed objects
per-class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Build.PL installdirs=vendor

./Build

%check
./Build test

%install
rm -rf %buildroot
./Build install destdir=%{buildroot}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 654933
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 471492
- import perl-Devel-LeakGuard-Object


* Sun Nov 29 2009 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist
