import os
import traceback

def get_files_info(working_directory, directory="."):
    # print(working_directory, directory)
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
        if not valid_target_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'
        
        files = []
        for file in os.listdir(target_dir):
            full_path = os.path.normpath(os.path.join(target_dir, file))
            files.append(f"{file}: file_size={os.path.getsize(full_path)} bytes, is_dir={os.path.isdir(full_path)}")
        files_info = "  - " + "\n  - ".join(files)
        return files_info
    except Exception as e:
        traceback.print_exc()
        return f"Error: {str(e)}"




    
                     

    
