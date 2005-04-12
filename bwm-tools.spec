Summary:	Bandwidth Management Tools
Name:		bwm-tools
Version:	0.2.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/bwm-tools/bwm_tools-%{version}.tar.bz2
# Source0-md5:	67d2303ec9d34fd319a94f96043ea2d3
URL:		http://bwm-tools.pr.linuxrulz.org/
BuildRequires:	libxml2-devel >= 2.5.0
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	pkgconfig
#BuildRequires:	-
#Requires:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bandwidth Management Tools is a total bandwidth management solution
for Linux and can be used for firewalling, traffic graphing, and
shaping. It is not based on any currently-available bandwidth
management software and supports packet queues, bursting, complex
traffic flow hierarchies, flow groups, traffic logging, and a simple
real-time monitoring front-end.


%prep
%setup -q -n bwm_tools-%{version}

#%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__gettextize}
#%%{__libtoolize}
#%%{__aclocal}
#%%{__autoconf}
#%%{__autoheader}
#%%{__automake}
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
#%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

#%{_datadir}/%{name}

# initscript and its config
#%attr(754,root,root) /etc/rc.d/init.d/%{name}
#%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}
