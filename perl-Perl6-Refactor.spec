%define upstream_name    Perl6-Refactor
Name:		perl-%{upstream_name}
Version:	0.02_01
Release:	1

Summary:	The great new Perl6::Refactor!
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Perl6-Refactor
Source0:	https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Perl6-Refactor-0.02_01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build::Compat)
BuildArch:	noarch

%description
The great new Perl6::Refactor!

%prep
%setup -q -n Perl6-Refactor-0.02_01

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build
%check
%make test || :

%install
%makeinstall_std

%files
%doc META.yml README Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

