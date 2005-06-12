Summary:	Scheme Interpreter/Compiler System
Summary(pl):	Interpreter/Kompilator systemu scheme
Name:		stklos
Version:	0.70
Release:	1
Group:		Development/Languages
License:	GPL
Source0:	http://dl.sourceforge.net/stklos/%{name}-%{version}.tar.gz
# Source0-md5:	65f94dbea4667f884896964d57b4d5e0
Patch0:		%{name}-bash.patch
URL:		http://www.stklos.org/
BuildRequires:	gc-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	gdk-pixbuf-gnome-devel
BuildRequires:	gmp-devel
BuildRequires:	openldap-devel
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

%description -l pl
STklos jest szybkim interpreterem bytecodu Scheme staraj±cym siê byæ
zgodnym z R5RS. Jest nastêpc± STk (interpetera Scheme zdolnego do
korzystania z toolkitu Tk).

STKlos udostêpnia rozszerzalne i efektywne rozszerzenia zorientowane
objektowo udostêpniaj±ce wielokrotne dziedziczenie, ogólne funkcje,
wielo-metody.

STklos udostêpnia tak¿e po³±czenia do GTK+ pozwalaj±ce tworzyæ GUI i
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
