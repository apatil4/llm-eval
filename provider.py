from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import logging

def call_api(prompt, options, context):
    # The 'options' parameter contains additional configuration for the API call.
    config = options.get('config', None)
    additional_option = config.get('additionalOption', None)
    if additional_option == 'llama':
        llm = LlamaCpp(
            model_path="models/llama-2-7b-chat.Q4_K_M.gguf",
            temperature=0.75,
            max_tokens=2000,
            top_p=1,
        )
    elif additional_option == 'phi':
        llm = LlamaCpp(
            model_path="models/phi-2.Q4_K_M.gguf",
            temperature=0.75,
            max_tokens=2000,
            top_p=1,
        )
    else:
        raise NotImplementedError("")

    output = llm(prompt)
    # The result should be a dictionary with at least an 'output' field.
    result = {
        "output": output,
    }
    return result