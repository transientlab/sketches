COLOR_PROMPT=1
SHARED_DIRECTORY=/home/share
SUDO=1

if [ $SUDO ]; then
{
    su -l root
    apt-get install sudo
    usermod -aG sudo $USER
}

if [ $COLOR_PROMPT ]; then
    {
    echo "export PS1='\[\e[38;5;10m\]\u\[\e[38;5;220m\]@\[\e[38;5;14m\]\h \[\e[38;5;33m\]\w \[\033[0m\]$ '" > /home/$USER/.profile
    }
fi

if [ $SHARED_DIRECTORY]; then
    echo "SHARED_DIRECTORY=$SHARED_DIRECTORY" > /home/$USER/.profile
    sudo apt install spice-vdagent spice-webdavd qemu-guest-agent &&
    sudo mkdir $SHARED_DIRECTORY &&

    # this needs to be corrected
    echo "sudo mount -t davfs http://127.0.0.1:9843/ $SHARED_DIRECTORY" > .profile
