%include	/usr/lib/rpm/macros.perl
%define	pdir	LWP
%define	pnam	Parallel
Summary:	LWP::Parallel perl module
Summary(pl):	Modu³ perla LWP::Parallel
Name:		perl-LWP-Parallel
Version:	2.54
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}UserAgent-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:  perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LWP::Parallel - module for parallel downloading.

%description -l pl
LWP::Parallel - modu³ do równoleg³ego poberania.

%prep
%setup -q -n %{pnam}UserAgent-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install t/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.SSL
%{perl_sitelib}/LWP/*.pm
%{perl_sitelib}/LWP/Parallel/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
