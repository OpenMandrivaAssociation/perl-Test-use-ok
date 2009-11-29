%define upstream_name	 Test-use-ok
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	%mkrel 1

Summary:	A visitor for Perl data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Provides:   perl(ok)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %{_mandir}/*/*
%{perl_vendorlib}/Test/*
%{perl_vendorlib}/ok.pm
