%{!?version: %define version %(cat version)}
%if 0%{?qubes_builder}
%define _builddir %(pwd)
%endif

%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		qubes-usb-proxy-dom0
Version:	%{version}
Release:	1%{?dist}
Summary:	USBIP wrapper to run it over Qubes RPC connection - dom0 files

Group:		System
License:	GPLv2
URL:		https://www.qubes-os.org/
BuildArch:  noarch

BuildRequires:	python3
Requires:	python3

%description
Dom0 files for Qubes USBIP wrapper. This includes Qubes tools integration.
This package also contains tests.

%install
make install-dom0 DESTDIR=${RPM_BUILD_ROOT}


%files
%attr(0664,root,qubes) %config(noreplace) /etc/qubes-rpc/policy/qubes.USB
%dir %{python3_sitelib}/qubesusbproxy-*.egg-info
%{python3_sitelib}/qubesusbproxy-*.egg-info/*
%{python3_sitelib}/qubesusbproxy


%changelog

