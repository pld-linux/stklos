Summary:	Scheme Interpreter/Compiler System
Summary(pl):	Interpreter/Kompilator systemu scheme
Name:		stklos
Version:	0.58
Release:	1
Group:		Development/Languages
License:	GPL
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	8ab599f6f0c51e9c1b9973b120d90ac2
URL:		http://www.stklos.org/
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gc-devel
BuildRequires:	gmp-devel
BuildRequires:	openldap-devel
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
STklos is a fast Scheme bytecode interpreter trying to conform to
R5RS. It is the successor of STk (a Scheme interpreter able to access
the Tk toolkit).

STklos provides an extensive and efficient Object Oriented extension
providing multiple inheritance, generic functions, multi-methods. Its
implementation relies on a CLOS-like Meta Object Protocol.

STklos also provides a connection to GTK+ allowing to make GUI in a
clean and easy way.

%description -l pl
STklos jest szybkim interpreterem bytecodu Scheme staraj±cym siê byæ
zgodnym z R5RS. Jest nastêpc± STk (interpetatorem Scheme zdolnym do
korzystania z toolkitu Tk).

STKlos udostêpnia rozszerzalne i efektywne rozszerzenia zorientowane
objektowo udostêpniaj±ce wielokrotne dziedziczenie, ogólne funkcje,
wielo-metody.

STklos udostêpnia tak¿e po³±czenia do GTK+ pozwalaj±ce tworzyæ GUI i
przejrzysty i prosty sposób.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags} `gdk-pixbuf-config --cflags`"
%configure \
	--enable-ldap
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog TODO PACKAGES-USED AUTHORS SUPPORTED-SRFIS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
%{_prefix}/lib/%{name}/%{version}
%{_datadir}/%{name}/%{version}
%{_includedir}/%{name}
%{_infodir}/%{name}*
