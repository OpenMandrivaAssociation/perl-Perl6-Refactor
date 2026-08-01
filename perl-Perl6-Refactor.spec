%define upstream_name    Perl6-Refactor
%define upstream_version 0.02_01
Name:perl-%{upstream_name}
Version:0.02_01
Release:12

Summary:The great new Perl6::Refactor!
License:GPL+ or Artistic
Group:Development/Perl
Url:https://metacpan.org/dist/Perl6-Refactor
Source0:https://cpan.metacpan.org/authors/id/A/AZ/AZAWAWI/Perl6-Refactor-0.02_01.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Module::Build)
BuildArch:noarch

%description
The great new Perl6::Refactor!

%prep
%setup -q -n Perl6-Refactor-0.02_01

%build
perl Build.PL --installdirs=vendor
./Build

%check
./Build test || :

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%files
%doc META.yml README Changes LICENSE
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/*
