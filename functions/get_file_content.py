import os
from .config import MAX_CHARS
from google.genai import types

schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists the contents of the specified file. If the file is longer than 10,000 characters, it will be truncated at 10,000 characters. The file is constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING, # VVVV - Change this
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_abs, file_path)

        if not full_file_path.startswith(working_directory_abs):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(full_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(full_file_path, "r") as f:
            file_content_string = f.read()
        
        if len(file_content_string) > MAX_CHARS:
            return f'{file_content_string[:MAX_CHARS]} \n[...File "{file_path}" truncated at 10000 characters]'

        return f'{file_content_string}'

    except Exception as e:
        print(f"Error: {e}")


