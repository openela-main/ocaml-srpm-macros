# OCaml has a bytecode backend that works on anything with a C
# compiler, and a native code backend available on a subset of
# architectures.  A further subset of architectures support native
# dynamic linking.
#
# This package contains a single file needed to define some RPM macros
# which are required before any SRPM is built.
#
# See also: https://bugzilla.redhat.com/show_bug.cgi?id=1087794

%global macros_dir %{_rpmconfigdir}/macros.d

Name:           ocaml-srpm-macros
Version:        6
Release:        6%{?dist}

Summary:        OCaml architecture macros
License:        GPLv2+

BuildArch:      noarch

Source0:        macros.ocaml-srpm

# NB. This package MUST NOT Require anything (except for dependencies
# that RPM itself generates).

%description
This package contains macros needed by RPM in order to build
SRPMS.  It does not pull in any other OCaml dependencies.


%prep


%build


%install
mkdir -p $RPM_BUILD_ROOT%{macros_dir}
install -m 0644 %{SOURCE0} $RPM_BUILD_ROOT%{macros_dir}/macros.ocaml-srpm


%files
%{macros_dir}/macros.ocaml-srpm


%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 6-6
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 6-5
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 06 2019 Richard W.M. Jones <rjones@redhat.com> - 6-1
- Remove support for native profiling, see:
  https://github.com/ocaml/ocaml/pull/2314

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 08 2017 Richard W.M. Jones <rjones@redhat.com> - 5-2
- Bump and rebuild.

* Tue Aug  8 2017 Richard W.M. Jones <rjones@redhat.com> - 5-1
- Add new macro ocaml_native_profiling.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov  8 2016 Richard W.M. Jones <rjones@redhat.com> - 4-1
- s390x is now a native architecture with OCaml 4.04 in Fedora >= 26.
- Add riscv64 as a native arch using out of tree backend.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  2 2014 Richard W.M. Jones <rjones@redhat.com> - 2-1
- Move macros to _rpmconfigdir (RHBZ#1093528).

* Tue Apr 22 2014 Richard W.M. Jones <rjones@redhat.com> - 1-1
- New package.
