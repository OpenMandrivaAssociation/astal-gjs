%global debug_package %{nil}

%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

%global _vpath_srcdir lang/gjs

Name:       astal-gjs
Version:    1~%{bumpver}.git%{astal_shortcommit}
Release:    1
Source0:    https://github.com/aylur/astal/archive/%{astal_commit}/%{name}-%{astal_shortcommit}.tar.gz
Summary:    Building blocks for creating custom desktop shells
URL:        https://github.com/aylur/astal
License:    LGPL-2.1-only
Group:      System/Libraries

BuildRequires:  meson
BuildRequires:  pkgconfig(astal-io-0.1)
BuildRequires:  pkgconfig(astal-3.0)
BuildRequires:  pkgconfig(astal-4-4.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  gobject-introspection
BuildRequires:  pkgconfig(gobject-introspection-1.0)

Requires:  pkgconfig(astal-io-0.1)
Requires:  pkgconfig(astal-3.0)
Requires:  pkgconfig(astal-4-4.0)

Supplements:    astal

%package    devel
Summary:    Development files for %{name}
Requires:   %{name} = %{version}-%{release}
%description devel
Development files for %{name}

%description
%summary

%prep
%autosetup -n astal-%{astal_commit} -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%{_datadir}/astal/*


%files devel
%{_libdir}/pkgconfig/*
