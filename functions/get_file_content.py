import os
from .config import MAX_CHARS

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


