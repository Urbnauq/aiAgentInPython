from google.genai import types
from .get_files_info import schema_get_files_info
from .get_file_content import schema_get_files_content
from .run_python import schema_run_python_file
from .write_file_content import schema_write_file_content

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
        schema_run_python_file,
        schema_write_file_content,
    ]
)