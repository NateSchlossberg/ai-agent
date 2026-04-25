import os
from config import *

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        file_in_working_dir = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs
        if not file_in_working_dir:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: File not found or is not a regular file: "{file_path}'
        f = open(target_file, 'r')
        content = f.read(READ_MAX_CHARS)
        if f.read(1):
            content += f'[...File "{file_path}" truncated at {READ_MAX_CHARS} characters]'
        return content
    except Exception as e:
        return f"Error: {str(e)}"
