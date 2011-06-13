%define name rake
%define version 0.8.7

Name: %{name}
Summary: Rake is a simple ruby build program with capabilities similar to make
Version: %{version}
Release: %mkrel 1
License: MIT
Group: Development/Ruby
Source: http://rubyforge.org/frs/download.php/56872/%{name}-%{version}.tgz
URL:	http://rubyforge.org/
BuildRequires: zip, ruby 
BuildRoot: %_tmppath/%{name}-%{version}-buildroot

%description
Rake is a build tool similar to the make program in many ways. But
instead of cryptic make recipes, Rake uses standard Ruby code to
declare tasks and dependencies. You have the full power of a modern
scripting language built right into your build tool.


%prep
%setup -q -n %{name}-%{version}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{ruby_sitelibdir}/rake
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_mandir}/man1/
mv lib/rake/* %{buildroot}%{ruby_sitelibdir}/rake/
mv bin/* %{buildroot}%{_bindir}/
mv doc/rake.1.gz %{buildroot}%{_mandir}/man1/

%files
%defattr(0755,root,root)
%{ruby_sitelibdir}/rake/
%{_bindir}/
%{_mandir}/man1/rake.1.*
%doc README TODO MIT-LICENSE CHANGES

%clean
rm -rf $RPM_BUILD_ROOT
