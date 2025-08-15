import os
from google.genai import types

schema_write_file_content = types.FunctionDeclaration(
    name="write_file_content",
    description="Write or overwrite file. The files are constrained to the working directory.",
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

def write_file_content(working_directory, file_path, content):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_abs, file_path)

        if not full_file_path.startswith(working_directory_abs):
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
        file_path_dir = os.path.dirname(file_path)

        full_path_new_dir = os.path.exists(os.path.join(working_directory_abs, file_path_dir))
        if not full_path_new_dir:
            os.makedirs(full_path_new_dir)

        with open(os.path.join(working_directory_abs, file_path), "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        print(f"Error: {e}")