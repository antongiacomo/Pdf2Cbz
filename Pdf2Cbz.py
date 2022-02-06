#!/usr/bin/env python3

import os
import os.path
import time
import shutil
from math import floor
from zipfile import ZipFile
from natsort import os_sorted
from pdf2image import convert_from_path as pdf_path_to_images

from UpdateHandler import UpdateHandler

class Pdf2Cbz:
    _input_folder_path = None
    _zip_file_name = None
    _image_output_path = None
    _cores_number = floor(os.cpu_count() / 2)

    _update_handler = UpdateHandler()

    def __init__(self, input_folder_path, zip_file_name = "pdf2cbz_file.cbz", image_output_path = "out"):
        self._input_folder_path = input_folder_path
        self._zip_file_name = zip_file_name
        self._image_output_path = image_output_path

    def set_cores_numeber(self, cores_numebr):
        self._cores_number = cores_numebr

    def set_update_handler(self, update_handler: UpdateHandler):
        self._update_handler = update_handler

    def create_out_directory_if_not_exists(self):
        if not os.path.exists(self._image_output_path):
            os.mkdir(self._image_output_path)

    def conver_pdf_page_to_image(self, filepath, i):

        print("Start convert {}".format(filepath))
        pdf_path_to_images(
            filepath,
            thread_count=self._cores_number,
            output_folder=self._image_output_path,
            output_file=f"comic_{i}_",
            fmt="JPEG",
        )
        print("Finished extracting images from {}".format(filepath))

    def convert_pdf2image_in_folder(self):
        
        files, files_count = select_files_from_path(self._input_folder_path, ".pdf")
        
        for i, file in enumerate(files):

            filepath = self._input_folder_path + os.sep + file

            self.conver_pdf_page_to_image(filepath, i)

            self._update_handler.update(i,files_count)

    def zip_images(self):

        zipObj = ZipFile(self._zip_file_name, "w")

        files = select_files_from_path(self._image_output_path, ".jpg")

        for file in files[0]:
                filepath = self._image_output_path + os.sep + file
                zipObj.write(filepath)

        zipObj.close()

    def delete_images(self):
        #os.remove(self._image_output_path)
        shutil.rmtree(self._image_output_path)

    def convert(self):

        start = time.time()

        self.create_out_directory_if_not_exists()
        self.convert_pdf2image_in_folder()
        self.zip_images()
        self.delete_images()
    
        end = time.time()
        print(f"Elapsed time: {end-start} s")

def select_files_from_path(folder_path, files_type):

    files = [f for f in os.listdir(folder_path) if (os.path.isfile(os.path.join(folder_path, f)) and f.endswith(files_type))]
    files = os_sorted(files)
    files_count = len(files)
    return files, files_count

