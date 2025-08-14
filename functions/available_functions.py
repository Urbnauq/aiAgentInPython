from google.genai import types
from .get_files_info import schema_get_files_info
from .get_file_content import schema_get_files_content

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_files_content,
    ]
)