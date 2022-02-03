#!/usr/bin/env python3

import os
import os.path
import time
from math import floor
from zipfile import ZipFile

from natsort import os_sorted
from pdf2image import convert_from_path as pdf_path_to_images

CORES = floor(os.cpu_count() / 2)
ROOTDIR = "source"



def main():

    create_out_directory_if_not_exists("out")

    start = time.time()



    for subdir, dirs, files in os.walk(ROOTDIR):
        files = os_sorted(files)

        for i, file in enumerate(files):

            filepath = subdir + os.sep + file
            print("Start convert {}".format(filepath))
            pdf_path_to_images(
                filepath,
                thread_count=CORES,
                output_folder="out",
                output_file=f"comic_{i}_",
                fmt="JPEG",
            )

            print("Finished extracting images from {}".format(filepath))

    mid = time.time()
    print(f"Mid time: {mid - start}")
    output_dir = "out"
    zipObj = ZipFile("sample.cbz", "w")

    for subdir, dirs, files in os.walk(output_dir):
        files = os_sorted(files)
        for file in files:
            filepath = subdir + os.sep + file
            zipObj.write(filepath)

    zipObj.close()
    end = time.time()

    print(f"Finishing time: {end-start}")

def create_out_directory_if_not_exists(out_directory):
    if not os.path.exists(out_directory):
        os.mkdir(out_directory)


if __name__ == "__main__":
    main()

