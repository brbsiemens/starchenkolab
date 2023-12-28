# Create RPM SPEC file (count_files.spec)
Name: my-count-files
Version: 1.0
Release: 1%{?dist}
Summary: Script to count files in /etc

%description
This script counts files in /etc.

%files
/usr/local/bin/count_files.sh

%changelog
* Mon Jan 01 2023 Ivan Vertebny <vanya.vertebny.0205@gmail.com> - 1.0-1
- Initial package
