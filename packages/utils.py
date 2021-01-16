import os
import shutil
from os.path import isdir  

def getFiles(dir):
    '''
        getFiles(dir)

        This function gets the files of the directory dir.
        It should be noted that this function just gets the files, it does not get the directories.

        Parameters
        ------------------------------------------------------------------------------------------
        dir: Directory to be scanned to find the files

        Returns
        ------------------------------------------------------------------------------------------
        files: List with the found files
    '''
    list = os.listdir(dir)
    files = []
    for file in list:
        if os.path.isfile(os.path.join(dir,file)):
            files.append(file)
    return files


# Funcion que coge las extensiones de los archivos y crea una carpeta para cada uno de ellos si no existe ya
def organizeFiles(files , dir):
    '''
        sortFiles(files, dir)

        This function sorts the files found in the "files" list,
        placing them into a directory according to their extension.

        Parameters
        ------------------------------------------------------------------------------------------
        files: List with the files
        dir: Directory to be organize
    '''
    extensions = []
    for file in files:
        _,ext = os.path.splitext(file)
        ext = ext.replace(".","")
        if not os.path.exists(os.path.join(dir,ext)):
            os.mkdir(os.path.join(dir,ext))
        shutil.move(os.path.join(dir,file),os.path.join(dir,ext))





