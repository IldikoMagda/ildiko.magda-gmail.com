import os
import shutil
from os import listdir
from os.path import isfile, join
download_folder = "/home/ildiko/Downloads"

def sort_myfiles_indownloads(foldertosort):
    """"This will be the function that sorts my folder"""
    files= [f for f in os.listdir(download_folder)if os.path.isfile(os.path.join(download_folder, f))]
    for eachfile in files:
        a= eachfile.rsplit('.',1)
        try:
            extname= (a[1], "folder")
            extfld = "_".join(extname)
            path= os.path.join(download_folder, extfld)
            if not os.path.exists(os.path.join(download_folder, extfld)):
                os.makedirs(path)

                current = os.path.join(download_folder, eachfile)
                destination = os.path.join(path, eachfile)
                shutil.move(current, destination)
            else:
                current = os.path.join(download_folder, eachfile)
                destination = os.path.join(path, eachfile)
                shutil.move(current, destination)
                
        except IndexError:
            continue


sort_myfiles_indownloads(download_folder)