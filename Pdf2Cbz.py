#!/usr/bin/env python3

from asyncio.windows_events import NULL
import os
import os.path
from os import listdir
from os.path import isfile, join
import time
from math import floor
from zipfile import ZipFile

from natsort import os_sorted
from pdf2image import convert_from_path as pdf_path_to_images

def select_files_from_path(folder_path, files_type):

    files = [f for f in listdir(folder_path) if (isfile(join(folder_path, f)) and f.endswith(files_type))]
    files = os_sorted(files)
    files_count = len(files)
    return files, files_count

def create_out_directory_if_not_exists(out_directory):
    if not os.path.exists(out_directory):
        os.mkdir(out_directory)

def conver_pdf_page_to_image(filepath, output_folder_path, i, cores = floor(os.cpu_count() / 2)):

    print("Start convert {}".format(filepath))
    pdf_path_to_images(
        filepath,
        thread_count=cores,
        output_folder=output_folder_path,
        output_file=f"comic_{i}_",
        fmt="JPEG",
    )
    print("Finished extracting images from {}".format(filepath))

def convert_pdf2image_in_folder(input_folder_path, output_folder_path):

    files = select_files_from_path(input_folder_path, ".pdf")
    print(files)
    for i, file in enumerate(files[0]):

        filepath = input_folder_path + os.sep + file

        conver_pdf_page_to_image(filepath, output_folder_path, i)

def zip_images(zip_file_name, output_folder_path):

    zipObj = ZipFile(zip_file_name, "w")

    files = select_files_from_path(output_folder_path, ".jpg")

    for file in files:
            filepath = output_folder_path + os.sep + file
            zipObj.write(filepath)

    zipObj.close()

def main():

    input_folder_path = "source2"
    output_folder_path = "out"
    zip_file_name = "sample.cbz"

    create_out_directory_if_not_exists(output_folder_path)

    start = time.time()

    convert_pdf2image_in_folder(input_folder_path, output_folder_path)

    mid = time.time()
    print(f"Mid time: {mid - start}")

    zip_images(zip_file_name, output_folder_path)
 
    end = time.time()
    print(f"Finishing time: {end-start}")


if __name__ == "__main__":
    main()

