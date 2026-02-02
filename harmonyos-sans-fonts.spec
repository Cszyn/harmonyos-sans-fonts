%global fontname harmonyos-sans
%global fontconf 69-%{fontname}.conf

Name:           %{fontname}-fonts
Version:        0
Release:        1%{?dist}
Summary:        HarmonyOS Sans fonts
License:        GPL-3.0-only
URL:            https://developer.huawei.com/consumer/en/design/resource/
Source0:        https://developer.huawei.com/Enexport/sites/default/images/download/next/HarmonyOS-Sans.rar

Packager:       Nagy András <aisen@ik.me>
BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  bsdtar
Requires:       fontpackages-filesystem

%description
HarmonyOS-Sans developed by Huawei predominantly used on HarmonyOS and OpenHarmony
devices, designed for a consistent multilingual typography in over a 100
languages.

%prep
%setup -q -c -T
bsdtar -xf %{SOURCE0}

%build

%install
install -m 0755 -d %{buildroot}%{_fontdir}
find . -name "*.ttf" -exec install -m 0644 {} %{buildroot}%{_fontdir} \;

%files
%dir %{_fontdir}
%{_fontdir}/*.ttf

%changelog
* Mon Feb 02 2026 Nagy András <aisen@ik.me> - 0-1
- Initial package
