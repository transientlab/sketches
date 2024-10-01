# =============================================
# Build-environment
# ==============================================
wget http://download.analog.com/tools/CrossCoreEmbeddedStudio/Releases/Release_2.10.1/adi-CrossCoreEmbeddedStudio-linux-x86-2.10.1.deb
sudo dpkg -i ./adi-CrossCoreEmbeddedStudio-linux-x86-2.10.1.deb

sudo apt-get update
sudo apt-get install -y gawk wget git-core diffstat unzip texinfo gcc-multilib build-essential chrpath socat libsdl1.2-dev xterm u-boot-tools openssl curl tftpd-hpa python lib32z1

mkdir ~/yocto-sc589
cd ~/yocto-sc589
mkdir bin
curl http://commondatastorage.googleapis.com/git-repo-downloads/repo > ./bin/repo
chmod a+x ./bin/repo
./bin/repo init \
  -u https://github.com/analogdevicesinc/lnxdsp-repo-manifest.git \
  -b release/yocto-2.1.0 \
  -m release-yocto-2.1.0.xml
./bin/repo sync

git config --global url."https://github.com".insteadOf git://github.com

# ==============================================
# Building image
# ==============================================

cd ~/yocto-sc589
source setup-environment adsp-sc589-mini
bitbake adsp-sc5xx-full

# ==============================================
# Configure TFTP, minicom
# ==============================================
sudo vi /etc/default/tftpd-hpa

# Replace the existing file with the following
# TFTP_USERNAME="tftp"
# TFTP_DIRECTORY="/tftpboot"
# TFTP_ADDRESS="0.0.0.0:69"
# TFTP_OPTIONS="--secure"
# End of File

sudo mkdir /tftpboot
sudo chmod 777 /tftpboot
sudo service tftpd-hpa restart


sudo apt-get install -y minicom
sudo minicom -s



#       +-----[configuration]------+
#       | Filenames and paths      |
#       | File transfer protocols  |
#       | Serial port setup        |
#       | Modem and dialing        |
#       | Screen and keyboard      |
#       | Save setup as dfl        |
#       | Save setup as..          |
#       | Exit                     |
#       | Exit from Minicom        |
#       +--------------------------+
#
#
# Select Serial port setup
#      Set Serial Device to /dev/ttyUSB0
#      Set Bps/Par/Bits to 115200 8N1
#      Set Hardware Flow Control to No
#  
#      Close the Serial port setup option by press Esc
#  Select Save setup as dfl
#  Select Exit
# ==============================================
