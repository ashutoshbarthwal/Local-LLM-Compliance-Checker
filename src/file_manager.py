import os
import json

class FileManager:
    def __init__(self, base_dir='docs'):
        self.base_dir = base_dir
        self.policy_dir = os.path.join(self.base_dir, 'policy')
        self.website_dir = os.path.join(self.base_dir, 'website')
        self.result_dir = os.path.join(self.base_dir, 'result')

        # Ensure directories exist
        os.makedirs(self.policy_dir, exist_ok=True)
        os.makedirs(self.website_dir, exist_ok=True)
        os.makedirs(self.result_dir, exist_ok=True)

    def save_to_file(self, directory, filename, content):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)

    def save_result(self, filename, result_data):
        result_filepath = os.path.join(self.result_dir, filename)
        with open(result_filepath, 'w', encoding='utf-8') as result_file:
            json.dump(result_data, result_file, indent=4)
