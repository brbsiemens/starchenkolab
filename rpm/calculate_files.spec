Name:           calculate_files
Version:        1.0
Release:        1%{?dist}
Summary:        A simple script to calculate files in a directory
Requires:       unzip

License:        MIT
URL:            https://github.com/brbsiemens/starchenkolab
Source0:        https://github.com/brbsiemens/starchenkolab/archive/main.zip'

BuildArch:      noarch

%description
calculate_files.sh is a simple script that calculates the number of files in a directory.

%prep
unzip %SOURCE0
cd starchenkolab-main

%install
mkdir -p %{buildroot}/usr/bin
install -m 755 %{_builddir}/starchenkolab-main/calculate_files.sh %{buildroot}/usr/bin/calculate_files

%files
/usr/bin/calculate_files

%changelog
* Sun Dec 23 2023 Starchenko Boris <starcenkoboris2@gmail.com> - 1.0-1
- Initial build
