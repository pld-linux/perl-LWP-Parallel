%include	/usr/lib/rpm/macros.perl
%define	pdir	LWP
%define	pnam	Parallel
Summary:	LWP::Parallel - module for parallel downloading
Summary(pl):	LWP::Parallel - modu³ do równoleg³ego pobierania
Name:		perl-LWP-Parallel
Version:	2.54
Release:	4
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pnam}UserAgent-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:  perl-libwww
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildConflicts:	perl-Attribute-Persistent < 1.0-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ParallelUserAgent (or PUA for short) is an extension of the existing
libwww-5.x distribution.  It allows you to connect to download several
Web pages in _parallel_, without having to request each page one after
the other.

%description -l pl
ParallelUserAgent (w skrócie PUA) to rozszerzenie istniej±cego pakietu
libwww-5.x. Pozwala na po³±czenie i ¶ci±ganie kilku stron WWW
_równolegle_, bez konieczno¶ci ¿±dania kolejnej strony po ¶ci±gniêciu
poprzedzniej.

%prep
%setup -q -n %{pnam}UserAgent-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install t/example* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README README.SSL
%{perl_sitelib}/LWP/*.pm
%{perl_sitelib}/LWP/Parallel
%{_mandir}/man3/LWP*
%{_examplesdir}/%{name}-%{version}
