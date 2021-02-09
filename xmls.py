# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:04:18 2021

@author: sunil.sharma
"""

import requests
import csv 
import xml.etree.ElementTree as ET
import zipfile
import os 

url = 'https://registers.esma.europa.eu/solr/esma_registers_firds_files/select?q=*&fq=publication_date:%5B2021-01-17T00:00:00Z+TO+2021-01-19T23:59:59Z%5D&wt=xml&indent=true&start=0&rows=100'
               
def loadRSS(url):
    
    # creating HTTP response object from given url 
    resp = requests.get(url)
    
    if resp.status_code != 200:
        raise APIerror("GET /task / {}".format(resp.status_code))
    
    else:
        # saving the xml file 
        with open('feed.xml', 'wb') as file:
             file.write(resp.content)
             

             
def parseXML(xmlfile):
    
    """This function change the root Node"""
    
    # create element tree object 
    tree = ET.parse(xmlfile) 
  
    # get root element 
    root = tree.getroot() 
        
    #creating the new_root
    New_root = root[1]
    
    return New_root
    
def getDownloadLink(root):
    
    """Provide the downloadable zip link"""
    try:
        for elem in root:
            for subelem in elem:
                print(subelem.attrib)
            
    except:
        print("Please check the root Node")
        
    #getting the download_link from new root node
    new_url =(root[0][1].text)   
    print(f"\n New url downloading link is : {new_url}")
    
    print("=====================")
    print("Please wait for few moment , New zip file is downloading...")
        
    return new_url

def downloadZip(url):
    """ Download the Zip file
        from url in current working directory with name
        DLNTS.zip """
        
    save_path = "DLNTS.zip"
    response = requests.get(url,stream=True)
    handle = open(save_path, 'wb')
    for chunk in response.iter_content(chunk_size = 512):
            if chunk :
                # Filter out chunks only
                handle.write(chunk)
     
    handle.close()
    print("\nFile has been download ")
    
def unzippingNewfile():
    
 #   current_path = os.getcwd()
    with zipfile.ZipFile('DLNTS.zip', 'r') as zip_ref:
        zip_ref.extractall(os.getcwd())
        
    print("Process is completed")
    print("\nPlease check the new Unzipped file in cureent directory  ")

            
        
def main():
    #load the XML
    loadRSS(url)
    
    #parse the XML
    rt = parseXML('feed.xml') 
    
    #Getting the new url
    N_url = getDownloadLink(rt)
    
    #Downloading new ZIP as DLNTS.zip
    downloadZip(N_url)
    
    #Unzip the New downloaded ZIP file in current directory
    unzippingNewfile()
    
    
    
if __name__ == "__main__":
    #calling the main function
    main()
       



  
    
   