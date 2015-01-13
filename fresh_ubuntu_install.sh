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
sudo apt-add-repository -y "deb http://repository.spotify.com stable non-free"
sudo apt-add-repository -y ppa:pidgin-developers/ppa
sudo tee -a deb http://cran.wustl.edu/bin/linux/ubuntu utopic/
echo 'deb http://download.videolan.org/pub/debian/stable/ /' | sudo tee -a /etc/apt/sources.list.d/libdvdcss.list
echo 'deb-src http://download.videolan.org/pub/debian/stable/ /' | sudo tee -a /etc/apt/sources.list.d/libdvdcss.list

## update, and upgrade base system
sudo apt-get update
sudo apt-get upgrade
sudo apt-get dist-upgrade


## install all the needed base packages
sudo apt-get install synaptic vlc gimp gimp-data gimp-pl
ugin-registry gimp-data-extras y-ppa-manager bleachbit oracle-java8-installer flashplugin-installer unace unrar zip unzip p7zip-full p7zip-rar sharutils rar uudeview mpack arj cabextract file-roller libxine1-ffmpeg mencoder flac faac faad sox ffmpeg2theora libmpeg2-4 uudeview libmpeg3-1 mpeg3-utils mpegdemux liba52-dev mpeg2dec vorbis-tools id3v2 mpg321 mpg123 libflac++6 totem-mozilla icedax lame libmad0 libjpeg-progs libdvdcss2 libdvdread4 libdvdnav4 libswscale-extra-2 ubuntu-restricted-extras spotify-client ubuntu-wallpapers* r-base r-base-dev python-pip python-setuptools inkscape filezilla git python-pandas pidgin openssh-server gparted

## install chrome 64-bit
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb &&
sudo dpkg -i google-chrome-stable_current_amd64.deb &&
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
echo "Cleaning Up" &&
sudo apt-get -f install &&
sudo apt-get autoremove &&
sudo apt-get -y autoclean &&
sudo apt-get -y clean
