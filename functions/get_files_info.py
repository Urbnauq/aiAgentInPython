import os

def get_files_info(working_directory, directory=None):
    full_path = os.path.join(working_directory, directory)
    
    try: 
        if os.listdir(os.path.abspath(directory)) == os.listdir(f"../{full_path}"):
          relative_path_directories = os.listdir(os.path.abspath(directory))
          for dr in relative_path_directories:
               print(f"- {dr}: file_size={os.path.getsize(dr)} bytes, is_dir={os.path.isdir(dr)}")
    except Exception:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    
working_directory = "aiAgentInPython"
directory = "calculator"
print(get_files_info(working_directory, directory))