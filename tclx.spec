#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : tclx
Version  : 1
Release  : 3
URL      : https://sourceforge.net/projects/tclx/files/TclX/8.4.1/tclx8.4.1.tar.bz2
Source0  : https://sourceforge.net/projects/tclx/files/TclX/8.4.1/tclx8.4.1.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : TCL
Requires: tclx-lib = %{version}-%{release}
Requires: tclx-license = %{version}-%{release}
Requires: tclx-man = %{version}-%{release}
BuildRequires : tcl
BuildRequires : tcl-dev
BuildRequires : tk
BuildRequires : tk-dev

%description
Extended Tcl (TclX) 8.4.1
=========================
INTRODUCTION
============
Extended Tcl (TclX), is an extension to Tcl, the Tool Command Language
invented by Dr. John Ousterhout.  Tcl is a powerful, yet simple embeddable
programming language.  Extended Tcl is oriented towards system programming
tasks and large application development.  TclX provides additional
interfaces to the operating system, and adds many new programming
constructs, text manipulation tools, and debugging tools.

%package dev
Summary: dev components for the tclx package.
Group: Development
Requires: tclx-lib = %{version}-%{release}
Provides: tclx-devel = %{version}-%{release}

%description dev
dev components for the tclx package.


%package lib
Summary: lib components for the tclx package.
Group: Libraries
Requires: tclx-license = %{version}-%{release}

%description lib
lib components for the tclx package.


%package license
Summary: license components for the tclx package.
Group: Default

%description license
license components for the tclx package.


%package man
Summary: man components for the tclx package.
Group: Default

%description man
man components for the tclx package.


%prep
%setup -q -n tclx8.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545260489
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1545260489
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tclx
cp license.terms %{buildroot}/usr/share/package-licenses/tclx/license.terms
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/tclx8.4/arrayprocs.tcl
/usr/lib64/tclx8.4/autoload.tcl
/usr/lib64/tclx8.4/buildhelp.tcl
/usr/lib64/tclx8.4/compat.tcl
/usr/lib64/tclx8.4/convlib.tcl
/usr/lib64/tclx8.4/edprocs.tcl
/usr/lib64/tclx8.4/events.tcl
/usr/lib64/tclx8.4/fmath.tcl
/usr/lib64/tclx8.4/forfile.tcl
/usr/lib64/tclx8.4/globrecur.tcl
/usr/lib64/tclx8.4/help.tcl
/usr/lib64/tclx8.4/pkgIndex.tcl
/usr/lib64/tclx8.4/profrep.tcl
/usr/lib64/tclx8.4/pushd.tcl
/usr/lib64/tclx8.4/setfuncs.tcl
/usr/lib64/tclx8.4/showproc.tcl
/usr/lib64/tclx8.4/stringfile.tcl
/usr/lib64/tclx8.4/tcllib.tcl
/usr/lib64/tclx8.4/tclx.tcl

%files dev
%defattr(-,root,root,-)
/usr/include/*.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/tclx8.4/libtclx8.4.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tclx/license.terms

%files man
%defattr(0644,root,root,0755)
/usr/share/man/mann/TclX.n
