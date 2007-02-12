Summary:	Scheme Interpreter/Compiler System
Summary(pl.UTF-8):	Interpreter/Kompilator systemu scheme
Name:		stklos
Version:	0.82
Release:	1
Group:		Development/Languages
License:	GPL
Source0:	http://dl.sourceforge.net/stklos/%{name}-%{version}.tar.gz
# Source0-md5:	2dad9823a2b34fd0dccc1a63a7978cbb
Patch0:		%{name}-bash.patch
URL:		http://www.stklos.org/
BuildRequires:	gc-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gmp-devel
BuildRequires:	openldap-devel >= 2.3.0
Requires:	bash
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

%description -l pl.UTF-8
STklos jest szybkim interpreterem bytecodu Scheme starającym się być
zgodnym z R5RS. Jest następcą STk (interpetera Scheme zdolnego do
korzystania z toolkitu Tk).

STKlos udostępnia rozszerzalne i efektywne rozszerzenia zorientowane
objektowo udostępniające wielokrotne dziedziczenie, ogólne funkcje,
wielo-metody.

STklos udostępnia także połączenia do GTK+ pozwalające tworzyć GUI i
przejrzysty i prosty sposób.

%prep
%setup -q
%patch0 -p1

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

%files
%defattr(644,root,root,755)
%doc README NEWS ChangeLog TODO PACKAGES-USED AUTHORS SUPPORTED-SRFIS
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/%{name}
%{_datadir}/%{name}
%{_includedir}/%{name}
%{_mandir}/man?/*
