Summary:	Statist is a terminal-based statistics program.
Name:		statist
Version:	1.4.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://statist.wald.intevation.org/
Source0:	http://wald.intevation.org/frs/download.php/301/statist-%{version}.tar.gz
Patch0:		statist-1.4.1-lang.patch
Requires:	gnuplot
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Statist is a terminal-based statistics program with an interactive menu that
makes it very easy to use. It can also be run in scripts and big datasets are
handled reasonably well even on small machines. In spite of its low overhead
statist can do quite a bunch of regression functions and tests. It can produce
colorized output and uses gnuplot to create graphics.

%prep
%setup -q
%patch0 -p1

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std PREFIX=%{buildroot}/usr

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING CREDITS KNOWN_BUGS README
%doc examples/
%{_bindir}/statist
%{_mandir}/*/*
%{_datadir}/locale/*/*/statist.mo
