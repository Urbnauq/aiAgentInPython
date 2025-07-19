import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    try:
        working_directory_abs = os.path.abspath(working_directory)
        full_file_path = os.path.join(working_directory_abs, file_path)
        
        if os.path.dirname(file_path) != "":
            if os.path.dirname(file_path) in os.listdir(working_directory_abs):
                if not full_file_path.startswith(working_directory_abs):
                    return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
            else:
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        else:
            if not full_file_path.startswith(working_directory_abs):
                return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.exists(full_file_path):
            return f'Error: File "{file_path}" not found.'
        
        if not full_file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        complete_process = subprocess.run(["uv", "run", full_file_path, *args], capture_output=True,timeout=30)

        output = []

        if complete_process.stdout == "":
            return "No output produced."

        if complete_process.stdout:
            output.append(f'STDOUT: {complete_process.stdout}')
        if complete_process.stderr:
            output.append(f'STDERR: {complete_process.stderr}')
        
        if complete_process.returncode != 0:
            output.append(f"Process exited with code {complete_process.returncode}")
            return "\n".join(output)
        
        return "\n".join(output)
        
    except Exception as e:
        print(f"Error: executing Python file: {e}")