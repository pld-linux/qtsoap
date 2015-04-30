Summary:	The Simple Object Access Protocol Qt-based client side library
Name:		qtsoap
Version:	2.7
Release:	1
License:	LGPLv2 with exceptions or GPLv3
Group:		Libraries
URL:		http://qt.gitorious.org/qt-solutions/qt-solutions/trees/master/qtsoap
# Source0:        http://get.qt.nokia.com/qt/solutions/lgpl/qtsoap-%{version}_1-opensource.tar.gz
Source0:	http://ftp.icm.edu.pl/packages/qt/solutions/lgpl/%{name}-%{version}_1-opensource.tar.gz
# Source0-md5:	3bb3c0ba836eccb94b6f75ba289b0213
Patch0:		%{name}-2.7_1-opensource-install-pub-headers.patch
BuildRequires:	QtCore-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The SOAP (Simple Object Access Protocol) library uses the XML standard
for describing how to exchange messages. Its primary usage is to
invoke web services and get responses from Qt-based applications.

%package        devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description    devel
Development files for %{name}.

%prep
%setup -q -n %{name}-%{version}_1-opensource

# headers are not installed for shared library
%patch0 -p1 -b .install-pub-headers

sed -i 's:$$DESTDIR:%{_libdir}:g' buildlib/buildlib.pro

%build
# we want shared library
echo "SOLUTIONS_LIBRARY = yes" > config.pri

echo "QTSOAP_LIBNAME = \$\$qtLibraryTarget(qtsoap)" >> common.pri
echo "VERSION=%{version}" >> common.pri

qmake-qt4 \
	PREFIX=%{_prefix}
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.TXT LGPL_EXCEPTION.txt
%attr(755,root,root) %ghost %{_libdir}/libqtsoap.so.2
%attr(755,root,root) %{_libdir}/libqtsoap.so.*.*

%files devel
%defattr(644,root,root,755)
%doc LGPL_EXCEPTION.txt
%attr(755,root,root) %{_libdir}/libqtsoap.so
%{_includedir}/qt4/QtSoap

%changelog
