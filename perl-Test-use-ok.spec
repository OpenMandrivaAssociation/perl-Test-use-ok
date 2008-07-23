%define module	Test-use-ok
%define name	perl-%{module}
%define version 0.02
%define	release	%mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A visitor for Perl data structures
License:	GPL or Artistic
Group:		Development/Perl
Source0:	%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %{module}-%{version}

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
%{perl_vendorlib}/Test/*
%{perl_vendorlib}/ok.pm
%doc %{_mandir}/*/*

