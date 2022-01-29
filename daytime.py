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
import tempfile
import zipfile
import pdb




# def get_pdf_photos(input_path, newZip):
# 	def empty_folder(folder_loc):
# 		for the_file in os.listdir(folder_loc):
# 			file_path = os.path.join(folder_loc, the_file)
# 			try:
# 				if os.path.isfile(file_path):
# 					os.unlink(file_path)
# 			except Exception as e:
# 				print(e)
# 				pdb.set_trace()

# 	def extract_information(pdf_path):
# 		try:
# 			with open(pdf_path, 'rb') as f:
# 				pdf = PdfFileReader(f)
# 				information = pdf.getDocumentInfo()
# 				number_of_pages = pdf.getNumPages()
# 				pageObj = pdf.getPage(0)
# 				full_text = pageObj.extractText()

# 			txt = f"""
# 			Information about {pdf_path}:
# 			Author: {information.author}
# 			Creator: {information.creator}
# 			Producer: {information.producer}
# 			Subject: {information.subject}
# 			Title: {information.title}
# 			Number of pages: {number_of_pages}
# 			"""
# 		except:
# 			information = '-'
# 			full_text = '-'

# 		return information, full_text

# 	# use tempfile for image processing
# 	print('\tgetting images from path...')
# 	with tempfile.TemporaryDirectory() as path:
# 		print('\t' + path)

# 		# use convert_from_path to create list of images
# 		# https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
# 		convert_from_path(pdf_path=input_path, fmt='jpeg', output_file = '', output_folder=path)

# 		print('\tgathered images.')

# 		for picture_name in os.listdir(path):
# 			# save image to zip file
# 			newZip.write(os.path.join(path, picture_name), arcname = picture_name, compress_type=zipfile.ZIP_DEFLATED)

# # function to create zip file and make cbz conversion more verbose
# def convert_pdf_to_comic(input_path, output_path):

# 	# interperet input path
# 	read_dir, file_name = os.path.split(input_path)
# 	cb_file_name = os.path.splitext(file_name)[0]

# 	# create zip file at working directory
# 	cb_file_path = os.path.join(output_path, cb_file_name + '.cbz')
# 	newZip = zipfile.ZipFile(cb_file_path, 'w')

# 	print('\t' + file_name)
# 	get_pdf_photos(input_path, newZip)

# 	# close zip file after completion
# 	newZip.close()
# 	print('\tsaved book', cb_file_name + '.cbz')

def image_to_file_buffer(images):
    fileImages = []
    for pil_image in images:
        file_object = io.BytesIO()
        pil_image.save(file_object, "PNG")
        fileImages.append(file_object)  # Replace PIL image object with BytesIO memory buffer.
        pil_image.close()

    return fileImages  # Return modified list.

def main():

    # Call the PdfFileMerger
    mergedObject = PdfFileMerger()
    
    #results = []
    rootdir = 'C:\\Users\\leota\\Desktop\\bbb' 

    for subdir, dirs, files in os.walk(rootdir):
        images = []
        for file in files:
            filepath = subdir + os.sep + file
            print('Start convert {}'.format(filepath))
            images.extend(pdf_path_to_images(filepath))
            print('Finished extracting images from {}'.format(filepath))
            images = image_to_file_buffer(images)
            print('Finished converting {}'.format(filepath))
            #mergedObject.append(PdfFileReader(filepath, 'rb'))

    # I had 116 files in the folder that had to be merged into a single document
    # Loop through all of them and append their pages
    zipFile = io.BytesIO()

    with ZipFile(zipFile, 'w') as zip_file:
        for image_name, bytes_stream in images:
            zip_file.writestr(image_name+".png", bytes_stream.getvalue())

    pprint(zip_file.infolist())  # Print final contents of in memory zip file.
    # Write all the files into a file which is named as shown below
    

    # pdf_list = [i for i in os.listdir(read_dir) if i.endswith('.pdf') == True]
    # no_of_pdfs = str(len(pdf_list))

    # n = 1
    # for read_file in pdf_list:

    #     input_path = os.path.join(read_dir, read_file)
    #     output_path = write_dir

    #     # initial checks
    #     assert os.path.exists(input_path) == True # check that file exists
    #     assert os.path.splitext(input_path)[1] == '.pdf' # check that file is pdf

    #     print('working on', n, 'of', no_of_pdfs)
    #     convert_pdf_to_comic(input_path, output_path)

    print('done.')


if __name__ == '__main__':
    main()
