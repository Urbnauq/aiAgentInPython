import os
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)

def get_files_info(working_directory, directory=None):
  try:
    full_path = os.path.abspath(os.path.join(working_directory, directory))
    dir_of_working_dir = os.listdir(full_path)

    working_dir_path = os.path.abspath(working_directory)
    if not full_path.startswith(working_dir_path):
      return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    results = []
    for dir in dir_of_working_dir:
      dir_path = os.path.abspath(os.path.join(full_path, dir))
      dir_is_dir = os.path.isdir(os.path.abspath(os.path.join(full_path, dir)))
      results.append(f"- {dir}: file_size={os.path.getsize(dir_path)} bytes, is_dir={dir_is_dir}")
    return "\n".join(results)
  
  except Exception as e:
    return f'Error: {e}'