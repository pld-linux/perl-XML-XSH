#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	XSH
Summary:	XML::XSH - an XML editing shell
Summary(pl):	XML::XSH - pow³oka do edycji XML-a
Name:		perl-XML-XSH
Version:	1.8.2
Release:	1
License:	GPL v2 or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c25f59c465f785347d0466d653d9893f
%if %{with tests}
BuildRequires:	perl-Parse-RecDescent >= 1.94
BuildRequires:	perl-XML-GDOME
BuildRequires:	perl-XML-LibXML >= 1.54
BuildRequires:	perl-XML-LibXML-XPathContext >= 0.04
BuildRequires:	perl-XML-LibXSLT >= 1.53
BuildRequires:	perl-XML-XUpdate-LibXML >= 0.4.0
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Parse-RecDescent >= 1.94
Requires:	perl-XML-LibXML >= 1.54
Requires:	perl-XML-LibXML-XPathContext >= 0.04
Requires:	perl-XML-LibXSLT >= 1.53
Requires:	perl-XML-XUpdate-LibXML >= 0.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xsh is a powerful command-line XML (DOM) editing tool/programming
language in the manner of Unix shell interpreters and line-oriented
text editors like ed. It can be used either interactively or for
batch-mode XML processing.

%description -l pl
xsh to potê¿ne dzia³aj±ce z linii poleceñ narzêdzie do edycji XML-a
(DOM), a tak¿e jêzyk programowania w stylu uniksowych pow³ok oraz
liniowo zorientowanych edytorów w stylu eda. Mo¿e byæ u¿ywane
interaktywnie lub do wsadowego przetwarzania XML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS ChangeLog Changes NOTES README TODO
%attr(755,root,root) %{_bindir}/xsh
%{perl_vendorlib}/XML/XSH.pm
%{perl_vendorlib}/XML/XSH
%{perl_vendorlib}/Inline/XSH.pm
%{_mandir}/man[13]/*
