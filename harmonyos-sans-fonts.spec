Name:           harmonyos-sans-fonts
Version:        25.09.23
Release:        2%?dist
Summary:        HarmonyOS Sans fonts
License:        LicenseRef-Proprietary
URL:            https://developer.huawei.com/consumer/cn/design/resource/
Source0:        https://alliance-communityfile-drcn.dbankcdn.com/FileServer/getFile/cmtyManage/011/111/111/0000000000011111111.20251218140934.53495826757772194907330661120530:50001231000000:2800:4C6B270E72171539BE152974FA4BAB1C2C63CB46549E9DC13D66B6F2BBC574CA.zip?needInitFileName=true

BuildArch:      noarch
BuildRequires:  fontpackages-devel
BuildRequires:  bsdtar
Requires:       fontpackages-filesystem
Packager:       N. András <aisen@ik.me>

%description
HarmonyOS-Sans developed by Huawei predominantly used on HarmonyOS and OpenHarmony
devices, designed for a consistent multilingual typography in over a 100
languages.

%prep
%setup -c -T
bsdtar -xf %{SOURCE0}

%build

%install
install -m 0755 -d %{buildroot}%{_datadir}/fonts/harmonyos-sans
find . -name "*.ttf" -exec install -m 0644 {} %{buildroot}%{_datadir}/fonts/harmonyos-sans/ \;

%files
%license LICENSE
%{_datadir}/fonts/harmonyos-sans/

%changelog
* Tue Feb 03 2026 N. András <aisen@ik.me> - 25.09.23-1
- Switched source to chinese developer portal release

* Mon Feb 02 2026 N. András <aisen@ik.me> - 24.06.19-1
- Initial package based on international developer portal release
