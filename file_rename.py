import glob
import os

for fileName in glob.glob('*mp4'):
    _, newFileName = fileName.split('#')
    os.rename(fileName,newFileName)