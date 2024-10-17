Summary:	Statist is a terminal-based statistics program
Name:		statist
Version:	1.4.1
Release:	5
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://statist.wald.intevation.org/
Source0:	http://wald.intevation.org/frs/download.php/301/statist-%{version}.tar.gz
Patch0:		statist-1.4.1-lang.patch
Patch1:		statist-1.4.1-flags.patch
Patch2:		statist-1.4.1-sfmt.patch
Patch3:		statist-1.4.1-no-strip.patch
Requires:	gnuplot

%description
Statist is a terminal-based statistics program with an interactive menu that
makes it very easy to use. It can also be run in scripts and big datasets are
handled reasonably well even on small machines. In spite of its low overhead
statist can do quite a bunch of regression functions and tests. It can produce
colorized output and uses gnuplot to create graphics.

%files -f %{name}.lang
%doc CHANGES COPYING CREDITS KNOWN_BUGS README
%doc examples/
%{_bindir}/statist
%{_mandir}/*/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
make \
	COMPILERCFLAGS="%{optflags} -c" \
	PREFIX=%{buildroot}%{_prefix}

%install
%makeinstall_std PREFIX=%{buildroot}%{_prefix}

%find_lang %{name}

