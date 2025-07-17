import os

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_abs, file_path)

        if not full_file_path.startswith(working_directory_abs):
            return f'Error: Cannot write "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if not full_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'

    except Exception as e:
        print(f"Error: {e}")