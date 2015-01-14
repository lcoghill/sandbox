## Simple shell script to setup a basic clean install of Fedora Linux with most of the core tools
## needed for my own daily use workstation. 
## I've tried to put things in sections so you can easily disable / remove anything you don't want.
## Tested on Fedora 21.

## Kill Tracker to save resources
sudo tracker-control -r

## Add Google Yum Repo - Need for Chrome etc.
touch /etc/yum.repos.d/google.repos
echo "[google64]" | sudo tee -a /etc/yum.repos.d/google.repos
echo "name=Google - x86_64"  | sudo tee -a /etc/yum.repos.d/google.repos
echo "baseurl=http://dl.google.com/linux/rpm/stable/x86_64"  | sudo tee -a /etc/yum.repos.d/google.repos
echo "enabled=1"  | sudo tee -a /etc/yum.repos.d/google.repos
echo "gpgcheck=1"  | sudo tee -a /etc/yum.repos.d/google.repos
echo "gpgkey=https://dl-ssl.google.com/linux/linux_signing_key.pub"  | sudo tee -a /etc/yum.repos.d/google.repos

## Install convenience software
sudo yum -y install google-chrome-stable
sudo yum -y install openssh-server
sudo yum -y install tmux
sudo yum -y install unzip
sudo yum -y install dos2unix
sudo yum -y install ncdu
sudo yum -y install filezilla
sudo yum -y install nano
sudo yum -y install vim
sudo yum -y install gvim
sudo yum -y install git
sudo yum -y install gnome-tweak-tool
sudo yum -y install yumex
sudo yum -y install pidgin
sudo yum -y install weechat
sudo yum -y install gparted
sudo yum -y install gimp
sudo yum -y install inkscape
sudo yum -y install dconf-editor
sudo yum -y install grub-customizer
sudo yum -y install nmap
sudo yum -y install wireshark-gnome


## VLC
sudo rpm -ivh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm
sudo yum -y install vlc

## Oracle JDK 8
## Need to update alternatives with sudo update-alternatives --config java / javac after install
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-pub/java/jdk/8u25-b17/jdk-8u25-linux-x64.rpm
sudo yum -y localinstall jdk-8u25-linux-x64.rpm
rm jdk-8u25-linux-x64.rpm
sudo alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 1
sudo alternatives --install /usr/bin/javac javac /usr/java/latest/bin/javac 1

## Install Microsoft Core Fonts
sudo yum -y rpm-build
sudo yum -y ttmkfdir
sudo yum -y cabextract
wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec
sudo rpmbuild -bb msttcorefonts-2.5-1.spec
sudo yum -y install /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm
rm msttcorefonts-2.5-1.spec

## Install FLASH from Adobe Repo
sudo rpm -ivh http://linuxdownload.adobe.com/adobe-release/adobe-release-x86_64-1.0-1.noarch.rpm
sudo rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-adobe-linux
sudo yum -y install flash-plugin 
sudo yum -y nspluginwrapper 
sudo yum -y alsa-plugins-pulseaudio 
sudo yum -y libcurl

## Install R and R Studio
sudo yum -y install r-devel
wget http://download1.rstudio.org/rstudio-0.98.1091-x86_64.rpm
sudo yum -y install rstudio-0.98.1091-x86_64.rpm
rm rstudio-0.98.1091-x86_64.rpm

## Update / Install Dev packages; GCC, Fortran, Python Packages, Ipython, Pandas etc...
sudo yum -y install gcc
sudo yum -y install gcc-c++
sudo yum -y install gcc-gfortran
sudo yum -y install python-setuptools
sudo yum -y install python-pip
sudo yum -y install python-biopython
sudo yum -y install scipy
sudo yum -y install ipython
sudo yum -y install python-pandas

## Install / Configure Python Graph-Tool
## This can take awhile, as it is compiling.
## Requires a decent amount of memory to compile.
wget http://downloads.skewed.de/graph-tool/graph-tool-2.2.36.tar.bz2
bunzip2 graph-tool-2.2.36.tar.bz2
tar -xvf graph-tool-2.2.36.tar.bz2
sudo yum -y install boost-devel
sudo yum -y install expat-devel
sudo yum -y install CGAL
sudo yum -y install CGAL-devel
wget https://sparsehash.googlecode.com/files/sparsehash-2.0.2-1.noarch.rpm
sudo yum -y localinstall sparsehash-2.0.2-1.noarch.rpm
rm sparsehash-2.0.2-1.noarch.rpm
sudo yum -y install pycairo
sudo yum -y install pycairo-devel
sudo yum -y install cairomm
sudo yum -y install cairomm-devel
cd graph-tool-2.2.36
sudo ./configure
sudo make
sudo make install
cd ..
sudo rm -r graph-tool-2.2.36
rm graph-tool-2.2.36.tar.bz2

## Install EOS Icon set
## Not needed, just a personal preference
sudo mkdir ~/.icons
wget -O eos-icons.tar.gz http://dl.dropbox.com/u/53319850/NoobsLab.com/eos-icons.tar.gz
tar -zxvf eos-icons.tar.gz -C ~/.icons
rm eos-icons.tar.gz

## Update with New Repos
sudo yum -y upgrade