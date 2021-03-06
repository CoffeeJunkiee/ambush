#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from geoip import geolite2
from datetime import datetime


class col:
    GRE  = '\033[92m'
    RED  = '\033[91m'
    YEL  = '\033[93m'
    END  = '\033[0m' 


def _print_ambush():
    print
    print '-' * 50
    print (col.GRE+'Date and Time:'+col.END), datetime.now()
    print('''
      ┌─┐┌┬┐┌┐ ┬ ┬┌─┐┬ ┬
      ├─┤│││├┴┐│ │└─┐├─┤
      ┴ ┴┴ ┴└─┘└─┘└─┘┴ ┴ IP locator''')
    print col.RED+'By:'+col.END, col.YEL+'InsaneGroove'+col.END
    print col.RED+'github.com/'+col.END, col.YEL+'InsaneGroove'+col.END
    print '-' * 50
    print
    
_print_ambush()

def work():
    
    time1 = datetime.now()
    time2 = datetime.now()
    total = time2 - time1
    
    _get = raw_input(col.GRE+'What\'s the IP?: '+col.END)
    
    if not _get:
        print '[*]Wrong input'
        work()        

    match = geolite2.lookup(_get)
    
    if match is not None:
        print(col.GRE+'country: '+col.END) , match.country
        print(col.GRE+'Continent: '+col.END) , match.continent
        print(col.GRE+'Time zone: '+col.END) , match.timezone
        print(col.GRE+'Subdivisions: '+col.END) , match.subdivisions
        print (col.GRE+'Finished location in: '+col.END), total 
        print
        print(col.RED+'Thanks for using Ambush.'+col.END)
        print
        
        sys.exit()
        
work()
