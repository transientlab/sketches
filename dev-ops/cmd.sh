ssh_configs() 
{

    # if ssh-agent is not running add this to .bashrc
    [ -z "$SSH_AUTH_SOCK" ] && eval "$(ssh-agent -s)"

    # generate key, type, Comment, file
    ssh-keygen -t ed25519 -C "kreispawel@gmail.com" -f github-key

    # add to ring
    ssh-add github-key

    # add id to remote machine
    ssh-copy-id -i {keyfile} user@host

    # add to github
    cat github-key.pub >> # [http://github.com -> Account/Settings/SSH and GPG/ -> Add new key]

    # in ~/.ssh/config add configuration for a host 
    # - add in host for github:
        ## Host github
        ##   Hostname github.com
        ##   User git
        ##   IdentityFile ~/.ssh/githubkey
    # - add in host for auto login to remote machine:
        ## Host i7w
        ## Hostname 174.128.0.2
        ## User kr315
        ## UserKnownHostsFile ~/.ssh/known_hosts_win
        ## IdentityFile ~/.ssh/win-i7


    # WINDOWS
    # System / Optional Features / OpenSSH Server & OpenSSH Authentication Agent
    # Services / OpenSSH Server / Automatic start & Start
    # in sshd_config remove line with administrators_authorized_keys
}

mqtt_stuff()
{

    MQTT_USER = 
    MQTT_PASS = 
    MQTT_SERV =
    MQTT_PORT = 
    sudo apt-get install mosquitto mosquitto-clients &&
    # subscribe to channel
    mosquitto_sub -h $MQTT_SERV -p $MQTT_PORT -u $MQTT_USER -P $MQTT_PASS -t /cmd/out &&
    # publish to channel
    mosquitto_pub -h $MQTT_SERV -p $MQTT_PORT -u $MQTT_USER -P $MQTT_PASS -t /cmd/out -m "value" &&

}


# workstation mac-address e0:d5:5e:41:6a:65
config_web_tools()
{
    sudo apt-get install curl wget git &&

    # node.js server
    sudo apt-get install npm &&
    sudo npm install express &&
    sudo npm install forever &&
}

conf_tools()
{
    # dev tools
    sudo apt-get install nvim openocd  minicom  &&
    sudo apt-get install build-essential gcc-arm-none-eabi libncurses-dev flex bison gperf python3 python-serial &&
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh


    # network tools
    sudo apt-get install arp-scan wakeonlan

    # multimedia
    sudo apt-get install ffmpeg
}

# airplay https://github.com/mikebrady/shairport-sync
configure_shairport()
{
    cd ~ &&
    sudo apt-get install autoconf libtool libdaemon-dev libasound2-dev libpopt-dev libconfig-dev -qy &&
    sudo apt install avahi-daemon libavahi-client-dev -qy &&
    sudo apt install libssl-dev -qy &&
    git clone https://github.com/mikebrady/shairport-sync.git &&
    cd shairport-sync &&
    autoreconf -i -f &&
    ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd --with-metadata &&
    make &&
    sudo make install &&
    sudo systemctl enable shairport-sync &&
    sudo service shairport-sync start
}

# ubuntu base station
# logitech
conf_ubuntu_base() 
{
    sudo apt-get install piper g810-led


    sudo add-apt-repository --yes ppa:kicad/kicad-8.0-releases
    sudo apt update
    sudo apt install --install-recommends kicad

    # graphics tools
    sudo apt-get install inkscape gimp librecad
}

# service
conf_service()
{
    sudo cp default.service /etc/systemd/system/test-app.service
}

colors()
{   
    # g213 keyboard
    sudo g810-led -r 0 00ff00
    sudo g810-led -r 4 ff0000
    sudo g810-led -r 5 0000ff

    # colorful bash
    export PS1='\[\e[38;5;10m\]\u\[\e[38;5;220m\]@\[\e[38;5;14m\]\h \[\e[38;5;33m\]\w \[\033[0m\]$ '

}

# system configs
debian_config()
{
    # add external packages
    sudo echo "deb http://deb.debian.org/debian/ sid main contrib non-free non-free-firmware" >> /etc/apt/sources.list &&
    sudo apt-get update &&
    sudo apt-get install nvidia-driver firmware-misc-nonfree &&

    # add to sudoers
    su -l root &&
    usermod -aG sudo ${username}

    # disable GUI
    sudo systemctl set-default multi-user

    # enable GUI
    sudo systemctl set-default graphical
}

# common commands
a_few_commands()
{
    if 0; then
    
        # capture / playback
        ffmpeg -f video4linux2 -i /dev/video0 out.mp4 -t 00:00:10       # capture camera input
        ffplay czesc.mp3 -nodisp -loop 1 -autoexit -af "volume=0.3"     # playback audio file

        ## clone image
        sudo dd if=/dev/mmcblk0 of=[mount point]/myimg.img bs=1M

        ## pc tools
        upower --enumerate | grep BAT
        brightnessctl
        

    fi
}

# qemu, davfs
vm_tools()
{
    if host; then
        # qemu virtual machine - host
        qemu-img create win10.hd.img.raw 48G

        qemu-system-x86_64 -bios OVMF.fd -enable-kvm -cpu host -smp 4 -m 2048 \
                            -cdrom Windows10_InsiderPreview_Client_x64_en-us_14332.iso \
                            -net nic,model=virtio -net user \
                            -drive file=win10.hd.img.raw,format=raw,if=virtio -vga qxl \
                            -drive file=virtio-win.iso,index=1,media=cdromqemu-system-x86_64 -bios OVMF.fd -enable-kvm -cpu host -smp 4 -m 2048 \
                            -cdrom Windows10_InsiderPreview_Client_x64_en-us_14332.iso \
                            -net nic,model=virtio -net user \
                            -drive file=win10.hd.img.raw,format=raw,if=virtio -vga qxl \
                            -drive file=virtio-win.iso,index=1,media=cdrom

        qeumu update definatealy
    fi

    # davfs - guest
    if guest; then
        mount -t davfs http://127.0.0.1:9843 /root/shared-host
    fi
}

# docker commands
docker_tools()
{

    docker run -ti ubuntu-t:latest /bin/bash
    docker run ls

}