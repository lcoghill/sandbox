#!/bin/bash
# Just a simple script to download all of the genbank flat files for eukaryotic organisms.
# It then combines those files into a single flat file for each dataset and decompresses them for use.
mkdir tempfiles
cd tempfiles
echo "Downloading INV flat files from genbank..."
wget -nv ftp://ftp.ncbi.nih.gov/genbank/gbinv*
clear
echo "Downloading MAM flat files from genbank..."
wget -nv ftp://ftp.ncbi.nih.gov/genbank/gbmam*
clear
echo "Downloading PLN flat files from genbank..."
wget -nv ftp://ftp.ncbi.nih.gov/genbank/gbpln*
clear
echo "Downloading PRI flat files from genbank..."
wget -nv ftp://ftp.ncbi.nih.gov/genbank/gbpri*
clear
echo "Downloading ROD flat files from genbank..."
wget -nv ftp://ftp.ncbi.nih.gov/genbank/gbrod*
clear
echo "Downloading VRT flat files from genbank..."
wget -nv ftp://ftp.ncbi.nih.gov/genbank/gbvrt*
echo "Complete."
clear
echo "Combining INV files..."
cat gbinv* > gbinv.seq.gz
mv gbinv.seq.gz ..
echo "Combining MAM files..."
cat gbmam* > gbmam.seq.gz
mv gbmam.seq.gz ..
echo "Combining PLN files..."
cat gbpln* > gbpln.seq.gz
mv gbpln.seq.gz ..
echo "Combining PRI files..."
cat gbpri* > gbpri.seq.gz
mv gbpri.seq.gz ..
echo "Combining ROD files..."
cat gbrod* > gbrod.seq.gz
mv gbrod.seq.gz ..
echo "Combining VRT files..."
cat gbvrt* > gbvrt.seq.gz
mv gbvrt.seq.gz ..
echo "Complete."
clear
echo "Cleaning up and Decompressing files..."
cd ..
rm -r tempfiles/
gunzip *.seq.gz
echo "Complete."
