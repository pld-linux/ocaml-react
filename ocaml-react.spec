#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	React - declarative events and signals for OCaml
Summary(pl.UTF-8):	React - deklaratywne zdarzenia i sygnały dla OCamla
Name:		ocaml-react
Version:	1.2.1
Release:	1
License:	ISC
Group:		Libraries
Source0:	https://erratique.ch/software/react/releases/react-%{version}.tbz
# Source0-md5:	ce1454438ce4e9d2931248d3abba1fcc
URL:		https://erratique.ch/software/react
BuildRequires:	ocaml >= 1:4.01.0
BuildRequires:	ocaml-findlib-devel
BuildRequires:	ocaml-ocamlbuild
BuildRequires:	ocaml-topkg-devel >= 0.9.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
React is an OCaml module for functional reactive programming (FRP). It
provides support to program with time varying values: declarative
events and signals. React doesn't define any primitive event or
signal, it lets the client choose the concrete timeline.

This package contains files needed to run bytecode executables using
OCaml react library.

%description -l pl.UTF-8
React to moduł OCamla do funkcyjnego programowania reaktywnego (FRP).
Wspiera programowanie z wartościami zmiennymi w czasie: deklaratywnymi
zdarzeniami i sygnałami. React nie definiuje żadnego podstawowego
zdarzenia czy sygnału, pozwala klientowi wybrać konkretną oś czasu.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki OCamla react.

%package devel
Summary:	React - declarative events and signals for OCaml - development part
Summary(pl.UTF-8):	React - deklaratywne zdarzenia i sygnały dla OCamla - część programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
react library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki react.

%prep
%setup -q -n react-%{version}

%build
ocaml pkg/pkg.ml build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/ocaml/react

cp -p _build/pkg/META _build/opam $RPM_BUILD_ROOT%{_libdir}/ocaml/react
cp -p _build/src/*.{cma,cmi,cmt,cmti,mli} $RPM_BUILD_ROOT%{_libdir}/ocaml/react
%if %{with ocaml_opt}
cp -p _build/src/*.{a,cmxs,cmx,cmxa} $RPM_BUILD_ROOT%{_libdir}/ocaml/react
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md TODO.md
%dir %{_libdir}/ocaml/react
%{_libdir}/ocaml/react/META
%{_libdir}/ocaml/react/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/react/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/react/*.cmi
%{_libdir}/ocaml/react/*.cmt
%{_libdir}/ocaml/react/*.cmti
%{_libdir}/ocaml/react/*.mli
%if %{with ocaml_opt}
%{_libdir}/ocaml/react/*.a
%{_libdir}/ocaml/react/*.cmx
%{_libdir}/ocaml/react/*.cmxa
%endif
%{_libdir}/ocaml/react/opam
