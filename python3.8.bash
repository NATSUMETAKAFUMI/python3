sudo apt update -y
sudo apt upgrade -y
sudo apt dist-upgrade
sudo apt autoremove -y
sudo apt autoclean -y

sudo apt install -y python3.8

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
sudo update-alternatives --config python3
