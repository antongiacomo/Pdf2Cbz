#!/usr/bin/env python3

from pdf2cbz import Pdf2Cbz

def main():

    input_folder_path = "source2"
    image_output_path = "out"
    zip_file_name = "sample.cbz"

    test = Pdf2Cbz(input_folder_path, zip_file_name, image_output_path)
    test.convert()


if __name__ == "__main__":
    main()

