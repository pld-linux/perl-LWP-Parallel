%include	/usr/lib/rpm/macros.perl
%define	pdir	LWP
%define	pnam	Parallel
Summary:	LWP::Parallel - module for parallel downloading.
Summary(pl):	LWP::Parallel - modu³ do równoleg³ego pobierania.
Name:		perl-LWP-Parallel
Version:	2.54
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pnam}UserAgent-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:  perl-libwww
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ParallelUserAgent (or PUA for short) is an extension of the existing
libwww-5.x distribution.  It allows you to connect to download several
Web pages in _parallel_, without having to request each page one after
the other.

# %description -l pl
# TODO

%prep
%setup -q -n %{pnam}UserAgent-%{version}

%build
perl Makefile.PL
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
