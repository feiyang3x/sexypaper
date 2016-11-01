#!/usr/bin/env python2
# -*- coding: UTF-8 -*-
import re
import urllib
import os
import time

url_home = 'http://www.sexy-beauties.com/morebabes.php?page='
url_top = 'http://www.sexy-beauties.com/'
def getwallpaper():
    page = 1
    while(page <= 140):
        url_page = url_home + str(page)
        page = page + 1
        html_data = urllib.urlopen(url_page)
        html_src = html_data.read()
        patt = re.compile('galleries.\w*.php' ,re.M)
        img_list = re.findall(patt, html_src)
        i = 0
        while(i < len(img_list)):
            url_last = url_top + img_list[i]
            html2_data = urllib.urlopen(url_last)
            html2_src = html2_data.read()
            ima_patt = re.compile('href="(.*?\d{2}.jpg)"', re.M)
            ima_list = re.findall(ima_patt, html2_src)
            print('This is page %d'%(i + 1))
            print('Page %d have: %d Pictures.'%(i + 1, len(ima_list)))
            i = i + 1
            j = 0
            while(j < len(ima_list)):
                print('This is No. %d'%(j + 1))
                print(ima_list[j])
                os.system('feh --bg-scale ' + ima_list[j])
                time.sleep(10000)
                j = j + 1
    return ima_list

if __name__ == '__main__':
    try:
        getwallpaper()
    except:
        KeyboardInterrupt
