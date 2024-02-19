from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts import PromptTemplate


# Callbacks support token-wise streaming
callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])

# Make sure the model path is correct for your system!
llama_llm = LlamaCpp(
    model_path="/Users/akshaypatil/hs/llm-eval/models/llama-2-7b-chat.Q4_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

phi_llm = LlamaCpp(
    model_path="/Users/akshaypatil/hs/llm-eval/models/phi-2.Q4_K_M.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
)

prompt = """
Question: Which is better team, Arsenal or Manchester United?
"""
print("------------ LLAMA OUTPUT -------------")

llama_llm.invoke(prompt)
print("\n\n")
print("------------ PHI OUTPUT -------------")
phi_llm(prompt)
