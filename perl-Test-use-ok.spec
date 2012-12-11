%define upstream_name	 Test-use-ok
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	A visitor for Perl data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

Provides:	perl(ok)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc %{_mandir}/*/*
%{perl_vendorlib}/Test/*
%{perl_vendorlib}/ok.pm

%changelog
* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.1
+ Revision: 471070
- adding missing provides:

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 399257
- rebuild
- using %%perl_convert_version
- fixed license & source0 fields

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.02-3mdv2009.0
+ Revision: 241985
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu May 03 2007 Michael Scherer <misc@mandriva.org> 0.02-1mdv2008.0
+ Revision: 21510
- update to 0.02


* Wed Mar 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.01-1mdk
- Initial MDV release

