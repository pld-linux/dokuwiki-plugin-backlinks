%define		plugin		backlinks
Summary:	DokuWiki Backlinks Plugin
Summary(pl.UTF-8):	Wtyczka backlinks dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	20080321
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://www.chimeric.de/_src/plugin-backlinks.tgz
# Source0-md5:	5ff0ac61d1f7438c13e64395a51364fe
URL:		http://www.dokuwiki.org/plugin:backlinks2
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir	/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
Lists all pages that link back to a given page using the first headline as link title.

%prep
%setup -q -n %{plugin}
if [ $(cat VERSION | tr -d -) != %{version} ]; then
	: %%{version} mismatch, should be: $(cat VERSION | tr -d -)
	exit 1
fi

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}
rm -f $RPM_BUILD_ROOT%{plugindir}/{COPYING,README,VERSION}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%doc README VERSION
%dir %{plugindir}
%{plugindir}/*.php
