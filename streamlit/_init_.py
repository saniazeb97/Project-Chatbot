import warnings
from langchain_community.llms import Ollama

# Ignore unnecessary warnings
warnings.filterwarnings("ignore")

# Initialize LLM with the desired model
llm = Ollama(model="llama2")

# Shared constants
UPLOAD_ENDPOINT = "http://127.0.0.1:8000/upload_pdf/"

# Expose for imports
__all__ = ["llm", "UPLOAD_ENDPOINT"]
