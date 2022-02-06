class UpdateHandler:
    
    @staticmethod
    def update_count(self, i, total_count):
        print(f"{i+1}/{total_count}")

    @staticmethod
    def start_pdf2image(self, filepath):
        print(f"Start conversion pdf2images of: {filepath}")

    @staticmethod
    def finish_pdf2image(self, filepath):
        print(f"Finished extracting images from {filepath}")


