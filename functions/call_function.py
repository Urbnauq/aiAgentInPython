from .get_files_info import get_files_info
from .get_file_content import get_file_content
from .run_python import run_python_file
from .write_file_content import write_file_content

from google.genai import types

def call_function(function_call_part, verbose=False):
    functions = {
        "get_files_info" : get_files_info,
        "get_file_content" : get_file_content,
        "run_python_file" : run_python_file,
        "write_file_content" : write_file_content,
    }

    function_name = function_call_part.name
    function_args = function_call_part.args
    
    if verbose:
        print(f"Calling function: {function_name}({function_args})")
    else:
        print(f" - Calling function: {function_name}")

    working_directory = "./calculator"
    function_args["working_directory"] = working_directory
    
    try:
        function_result = functions[function_name](**function_args)
        return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
    except:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )