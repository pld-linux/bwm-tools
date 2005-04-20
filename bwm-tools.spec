Summary:	Bandwidth Management Tools
Summary(pl):	Narz�dzia do zarz�dzania pasmem
Name:		bwm-tools
Version:	0.2.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/bwm-tools/bwm_tools-%{version}.tar.bz2
# Source0-md5:	1ca23ec25369057254b9ee24f0a2d1c7
URL:		http://bwm-tools.pr.linuxrulz.org/
BuildRequires:	autoconf
BuildRequires:	cgilibc-devel
BuildRequires:	gd-devel
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	libxml2-devel >= 2.5.0
BuildRequires:	ncurses-ext-devel
BuildRequires:	pkgconfig
BuildRequires:	rrdtool-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bandwidth Management Tools is a total bandwidth management solution
for Linux and can be used for firewalling, traffic graphing, and
shaping. It is not based on any currently-available bandwidth
management software and supports packet queues, bursting, complex
traffic flow hierarchies, flow groups, traffic logging, and a simple
real-time monitoring front-end.

%description -l pl
Bandwidth Management Tools to kompletne rozwi�zanie zarz�dzania pasmem
dla Linuksa, kt�re mo�e by� u�ywane� do zap�r sieciowych, wykres�w
ruchu oraz ograniczania pasma. Nie jest oparte na �adnym dotychczas
dost�pnym oprogramowaniu do zarz�dzania pasmem i obs�uguje kolejki
pakiet�w, strumienie, z�o�one hierarchie przep�ywu ruchu, grupy
przep�yw�w, logowanie ruchu oraz prosty frontend do monitorowania w
czasie rzeczywistym.

%prep
%setup -q -n bwm_tools-%{version}

%build
%{__autoconf}
%configure
%{__make} \
    CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/bwm_tools
install doc/example.xml $RPM_BUILD_ROOT%{_sysconfdir}/bwm_tools/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%{_infodir}/bwmtools.info*

%attr(750,root,root) %dir %{_sysconfdir}/bwm_tools/
%attr(640,root,root) %{_sysconfdir}/bwm_tools/example.xml

%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/libbwm*

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
