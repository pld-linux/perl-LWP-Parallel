%include	/usr/lib/rpm/macros.perl
%define		pdir	LWP
%define		pnam	Parallel
Summary:	LWP::Parallel - module for parallel downloading
Summary(pl.UTF-8):	LWP::Parallel - moduł do równoległego pobierania
Name:		perl-LWP-Parallel
Version:	2.57
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/ParallelUserAgent-%{version}.tar.gz
# Source0-md5:	7a1c42fbeee403606063f9ea7c691ed1
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	'perl(UNIVERSAL)'

%description
ParallelUserAgent (or PUA for short) is an extension of the existing
libwww-5.x distribution.  It allows you to connect to download several
Web pages in _parallel_, without having to request each page one after
the other.

%description -l pl.UTF-8
ParallelUserAgent (w skrócie PUA) to rozszerzenie istniejącego pakietu
libwww-5.x. Pozwala na połączenie i ściąganie kilku stron WWW
_równolegle_, bez konieczności żądania kolejnej strony po ściągnięciu
poprzedzniej.

%prep
%setup -q -n %{pnam}UserAgent-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.SSL
%{perl_vendorlib}/LWP/*.pm
%{perl_vendorlib}/LWP/Parallel
%{_mandir}/man3/LWP*
%{_examplesdir}/%{name}-%{version}
