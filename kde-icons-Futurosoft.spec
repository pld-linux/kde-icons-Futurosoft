%define		_name Futurosoft

Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0.5.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://i-soldi.com/futurosoft//%{_name}-Icons-%{version}.tar.gz
# Source0-md5:	c342c2a898911b00b1a6e26626dad771
URL:		http://www.kde-look.org/content/show.php?content=50667
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This icon theme is inspired by Vista.

%description -l pl.UTF-8
Jest to motyw oparty na Windows Vista.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfz %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
