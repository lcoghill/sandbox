## add several keys needed for repositories and packages
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 94558F59
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
wget -O - http://download.videolan.org/pub/debian/videolan-apt.asc | sudo apt-key add -

## add repositories or sources to /etc/apt/sources.list
sudo add-apt-repository -y ppa:videolan/stable-daily
sudo add-apt-repository -y ppa:otto-kesselgulasch/gimp
sudo add-apt-repository -y ppa:gnome3-team/gnome3
sudo add-apt-repository -y ppa:webupd8team/java
sudo add-apt-repository -y ppa:webupd8team/y-ppa-manager
sudo add-apt-repository -y ppa:transmissionbt/ppa
sudo apt-add-repository -y ppa:pidgin-developers/ppa
sudo echo -e "\n## Spotify Archive" | sudo tee -a /etc/apt/sources.list
sudo echo "deb http://repository.spotify.com/ stable non-free" | sudo tee -a /etc/apt/sources.list
sudo echo -e "\n## R Cran Archive" | sudo tee -a /etc/apt/sources.list
sudo echo "deb http://cran.wustl.edu/bin/linux/ubuntu/ utopic/" | sudo tee -a /etc/apt/sources.list
sudo echo -e "\ndeb http://download.videolan.org/pub/debian/stable/ /" | sudo tee -a /etc/apt/sources.list
sudo echo "deb http://download.videolan.org/pub/debian/stable/ /" | sudo tee -a /etc/apt/sources.list

## update, and upgrade base system
sudo apt-get --yes update
sudo apt-get --yes upgrade
sudo apt-get --yes dist-upgrade


## install all the needed base packages
sudo apt-get --yes install synaptic 
sudo apt-get --yes install vlc 
sudo apt-get --yes install gimp gimp-data gimp-plugin-registry gimp-data-extras 
sudo apt-get --yes install y-ppa-manager 
sudo apt-get --yes install bleachbit 
sudo apt-get --yes install oracle-java8-installer 
sudo apt-get --yes install flashplugin-installer 
sudo apt-get --yes install unace 
sudo apt-get --yes install rar unrar 
sudo apt-get --yes install zip unzip  
sudo apt-get --yes install p7zip-full p7zip-rar 
sudo apt-get --yes install sharutils 
sudo apt-get --yes install uudeview 
sudo apt-get --yes install mpack 
sudo apt-get --yes install arj 
sudo apt-get --yes install cabextract 
sudo apt-get --yes install file-roller 
sudo apt-get --yes install libxine1-ffmpeg 
sudo apt-get --yes install mencoder 
sudo apt-get --yes install flac faac faad 
sudo apt-get --yes install sox 
sudo apt-get --yes install ffmpeg2theora 
sudo apt-get --yes install libmpeg2-4 
sudo apt-get --yes install uudeview 
sudo apt-get --yes install libmpeg3-1 
sudo apt-get --yes install mpeg3-utils 
sudo apt-get --yes install mpegdemux 
sudo apt-get --yes install liba52-dev 
sudo apt-get --yes install mpeg2dec 
sudo apt-get --yes install vorbis-tools 
sudo apt-get --yes install id3v2 
sudo apt-get --yes install mpg321 
sudo apt-get --yes install mpg123 
sudo apt-get --yes install libflac++6 
sudo apt-get --yes install totem-mozilla 
sudo apt-get --yes install icedax 
sudo apt-get --yes install lame 
sudo apt-get --yes install libmad0 
sudo apt-get --yes install libjpeg-progs 
sudo apt-get --yes install libdvdcss2 
sudo apt-get --yes install libdvdread4 
sudo apt-get --yes install libdvdnav4 
sudo apt-get --yes install libswscale-extra-2 
sudo apt-get --yes install ubuntu-restricted-extras 
sudo apt-get --yes install spotify-client 
sudo apt-get --yes install ubuntu-wallpapers 
sudo apt-get --yes install r-base r-base-dev 
sudo apt-get --yes install python-pip python-setuptools python-pandas 
sudo apt-get --yes install inkscape 
sudo apt-get --yes install filezilla 
sudo apt-get --yes install git
sudo apt-get --yes install pidgin 
sudo apt-get --yes install openssh-server 
sudo apt-get --yes install gparted

## install chrome 64-bit
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
rm -f google-chrome-stable_current_amd64.deb

## install sublime text 3
wget http://c758482.r82.cf2.rackcdn.com/sublime-text_build-3065_amd64.deb
sudo dpkg -i sublime-text_build-3065_amd64.deb
rm -f sublime-text_build-3065_amd64.deb

## install r-studio
wget http://download1.rstudio.org/rstudio-0.98.1091-amd64.deb
sudo dpkg -i rstudio-0.98.1091-amd64.deb
rm -f rstudio-0.98.1091-amd64.deb

## clean up after all the installs
echo "Cleaning Up"
sudo apt-get -f install
sudo apt-get autoremove
sudo apt-get -y autoclean
sudo apt-get -y clean