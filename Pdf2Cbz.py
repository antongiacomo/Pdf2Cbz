#!/usr/bin/env python3

import os
import io
from PIL import Image
from pprint import pprint
from zipfile import ZipFile
import os.path
from PyPDF2 import PdfFileMerger, PdfFileReader
from pdf2image import convert_from_path as pdf_path_to_images
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError
)
from natsort import os_sorted
import tempfile
import zipfile
import pdb
import time

cores = 6 #os.cpu_count()/2
out_directory = "out"
if not os.path.exists(out_directory):
    os.mkdir("out")

def main():

    start = time.time()
    rootdir = 'source' 
    
    for subdir, dirs, files in os.walk(rootdir):
        files = os_sorted(files)

        for i, file in enumerate(files):
            
            images = []
            filepath = subdir + os.sep + file
            print('Start convert {}'.format(filepath))
            images.extend(pdf_path_to_images(filepath, thread_count= cores , output_folder="out", output_file=f"comic_{i}_", fmt="JPEG" ))
            print('Finished extracting images from {}'.format(filepath))

    mid = time.time()
    print(f'Mid time: {mid - start}')
    output_dir = 'out'
    zipObj = ZipFile('sample.zip', 'w')

    for subdir, dirs, files in os.walk(output_dir):
        files = os_sorted(files)
        for file in files: 
            filepath = subdir + os.sep + file    
            zipObj.write(filepath)

    zipObj.close()
    end = time.time()

    print(f'Finishing time: {end-start}')
    


if __name__ == '__main__':
    main()
