import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.normpath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))
        file_in_working_dir = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs
        if not file_in_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not file_path_abs.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file'
        command = ["python", file_path]
        if args:
            command.extend(args)
        # print("COMMAND: ", " ".join(command))
        result = subprocess.run(
            args=command, 
            cwd=working_dir_abs,
            text=True,
            capture_output=True,
            timeout=30
        )
        outputs = []
        if result.returncode != 0:
            outputs.append(f"Process exited with code {result.returncode}")
        if not result.stdout and not result.stderr:
            outputs.append("No output produced")
        else:
            if result.stdout:
                outputs.append(f'STDOUT: {result.stdout}')
            if result.stderr:
                outputs.append(f'STDERR: {result.stderr}')
        return "\n".join(outputs)
    except Exception as e:
         return f"Error: executing Python file: {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run a python file through a python3 interpreter (relative to the working directory) and returns the results, including any non-zero exit code, STDOUT, and STDERR",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to python file to run, relative to the working directory.  Filename must end in '.py'",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Argument to pass into python file",
                ),
                description="Array of arguments to pass to the python file upon execution. Arguments will be appended in order of the array",
            ),
        },
        required=["file_path"],
    ),
)
    
    

