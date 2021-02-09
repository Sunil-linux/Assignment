# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 23:48:23 2021

@author: sunil.sharma
"""

import xml.etree.ElementTree as ET
import pandas as pd

xml_data = open('DLTINS_20210117_01of01.xml', 'rb').read()  # Read file
root = ET.XML(xml_data)




#changing the root

root2 = root[1][0][0][2][0][0]
print(root2)

#length of childern in 'FinInstrmGnlAttrbts'
len(root2.getchildren())

for elem in root2:
        print(elem)
    

        



