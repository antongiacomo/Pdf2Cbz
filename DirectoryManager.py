#!/usr/bin/env python3

import os
import os.path
import shutil

class DirectoryManager:

    @staticmethod
    def create_out_directory_if_not_exists(image_output_path):
        if not os.path.exists(image_output_path):
            os.mkdir(image_output_path)

    @staticmethod
    def delete_images_folder(image_output_path):
        #os.remove(self._image_output_path)
        shutil.rmtree(image_output_path)

    @staticmethod
    def check_is_file_and_type(file, folder_path, files_type):
        if (os.path.isfile(os.path.join(folder_path, file)) and file.endswith(files_type)):
            return True
        else:
            return False

