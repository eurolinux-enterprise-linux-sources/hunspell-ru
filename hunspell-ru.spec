Name: hunspell-ru
Summary: Russian hunspell dictionaries
Version: 0.99g5
Release: 5%{?dist}
Epoch: 1
Source: http://releases.mozilla.org/pub/mozilla.org/addons/3703/russian_spellchecking_dictionary-0.4.4-fx+tb+sm.xpi
Group: Applications/Text
URL: http://scon155.phys.msu.su/eng/lebedev.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: BSD
BuildArch: noarch

Requires: hunspell

%description
Russian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-ru

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p dictionaries/ru.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/ru_RU.dic
cp -p dictionaries/ru.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/ru_RU.aff
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
ru_RU_aliases="ru_UA"
for lang in $ru_RU_aliases; do
        ln -s ru_RU.aff $lang.aff
        ln -s ru_RU.dic $lang.dic
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc dictionaries/Changelog dictionaries/LICENSE dictionaries/README
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1:0.99g5-5
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.99g5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.99g5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.99g5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jul 12 2011 Caolán McNamar <caolanm@redhat.com> 1:0.99g5-1
- Resolves: rhbz#716594 use 0.99g5 ff conversion, take 2

* Fri Jul 01 2011 Caolán McNamar <caolanm@redhat.com> 1:0.99f7-6
- Resolves: rhbz#716594 use yo variant

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.99f7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.99f7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.99f7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Jan 21 2009 Caolán McNamara <caolanm@redhat.com> - 1:0.99f7-2
- add alias

* Tue Aug 21 2007 Caolán McNamara <caolanm@redhat.com> - 1:0.99f7-1
- clarify licence
- canonical upstream source

* Thu Dec 07 2006 Caolán McNamara <caolanm@redhat.com> - 0.20040406-1
- initial version
