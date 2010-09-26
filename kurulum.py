#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################
# bir sistem kurulumu sonrasında gerekli temel paketler kurulumu
# istediğinizi seçip istediğinizi kaldırabilirsiniz
#
# emineker                                              gruop 19
################################################################


import os

def yukle():
        os.system('sudo apt-get install vlc vim mc zip rar byzanz')     # bazı gerekli paketler
        os.system('sudo apt-get install ubuntu-restricted-extra')       # ubuntu gerekli extra pektlerinin tümü 
        os.system('sudo apt-get install flashplugin-nonfree-extrasound')# flash player
        os.system('sudo apt-get install w32codecs libdvdcss2')          # media codec-leri
        os.system('sudo apt-get install flashplugin-nonfree')           # internet ortamı gerekli flash paketleri
        os.system('sudo apt-get install sun-java6-jdk')                 # java
        os.system('sudo apt-get install ssh')                           # uzaktan erişim paketi
        os.system('sudo apt-get install curl github-cli')               # github için
        os.system('sudo aptitude install sun-java6-jre sun-java6-plugin')                               # lime wire için gerekli paket
        os.system('sudo apt-get install python-mysqldb python-imaging python-pypdf python-reportlab')   # python paketleri
        os.system('aptitude install mysql-server mysql-client mysql-query-browser')                     # mysql ve extra paketleri kurulumu

        os.system('sudo apt-get upgrade')                               # sistem güncellemesini gerçekleştirir
        os.system('sudo apt-get update')                                # tüm paketleri günceller
        os.system('sudo apt-get -f install')                            # yarım kalan paketleri tamamlar


def vim():
        # programlama için gerekli vim ayarları; python, c ve ruby derlemek için kısayollar
        kaynak = ['syntax enable' ,
                  'filetype indent on' , 
                  'set et'  , 
                  'set sw=8' , 
                  'set smarttab' , 
                  'map <f2> :w\|!python %<cr>' ,
                  'map <f3> :w\|!gcc %<cr>' ,
                  'map <f4> :w\|!ruby %<cr>' ]

        with open('/home/' + os.getlogin() + '/.vimrc' , 'w') as dosya:
                [dosya.write(i+'\n') for i in kaynak]


def dns():
        # dns değiştir
        kaynak = ['# Generated by NetworkManager' ,
                  'nameserver 156.154.70.22' ,
                  'nameserver 156.154.71.22' ]

        with open('/etc/resolv.conf' , 'w') as dosya:
                [dosya.write(i+'\n') for i in kaynak]


if __name__ == "__main__":
        yukle()
        vim()
        dns()
        raw_input('sistem yeniden başlatılacak... >Enter<')
        os.system('sudo reboot')

