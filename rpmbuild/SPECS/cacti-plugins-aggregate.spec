Summary:	Plugin CACTI aggregate
Name:		cacti-plugins-aggregate
Version:	0.75
Release:    	1.bdi6
Group:		System/Monitoring
License:	GPLv2
Source0:	cacti-plugins-aggregate-%{version}.tgz
BuildRoot:  	%(mktemp -ud %{_tmppath}/}%{name}-XXXXXX)
BuildArch:	noarch
Requires:	cacti

%description
Plugin CACTI aggregate

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/cacti/plugins/aggregate/
cp -p * %{buildroot}/usr/share/cacti/plugins/aggregate/


%clean
rm -rf %{buildroot}


%files
%defattr(-,cacti,cacti,-)
%doc /usr/share/cacti/plugins/aggregate/LICENSE
%doc /usr/share/cacti/plugins/aggregate/README
%doc /usr/share/cacti/plugins/aggregate/aggregate_manual.pdf
/usr/share/cacti/plugins/aggregate/*.php


%changelog
* Tue Apr 8 2014 Marco Tizzoni <marco.tizzoni@gmail.com> 0.75-1
- Add %doc flag
