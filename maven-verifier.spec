%global pkg_name maven-verifier
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        1.4
Release:        6.12%{?dist}
Summary:        Maven verifier
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-verifier
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
# Forwarded upstream, see MSHARED-284
Patch1:         0001-Update-to-maven-shared-utils-0.3.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}maven-surefire-provider-junit
BuildRequires:  %{?scl_prefix}maven-shared
BuildRequires:  %{?scl_prefix}maven-shared-utils


%description
Provides a test harness for Maven integration tests.

This is a replacement package for maven-shared-verifier

%package javadoc
Summary:        Javadoc for %{pkg_name}
    
%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%patch1 -p1
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%{_javadir}/%{pkg_name}
%dir %{_mavenpomdir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 1.4-6.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.4-6.11
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.4-6.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.4-6.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.4
- Add missing BR: maven-shared

* Mon Feb 17 2014 Michal Srb <msrb@redhat.com> - 1.4-7.2
- SCL-ize BR

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-6.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.4-6
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Apr 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.4-4
- Update to maven-shared-utils 0.3

* Fri Feb 08 2013 Tomas Radej <tradej@redhat.com> - 1.4-3
- Building the new way

* Thu Jan 24 2013 Tomas Radej <tradej@redhat.com> - 1.4-2
- Added BuildRequires on maven-shared-utils

* Wed Jan 16 2013 Tomas Radej <tradej@redhat.com> - 1.4-1
- Initial version

