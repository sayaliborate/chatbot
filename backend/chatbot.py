# from langchain_openai import ChatOpenAI
# from langchain_core.messages import HumanMessage
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-3.5-turbo",
#     temperature=0.7
# )

# def get_response(message: str) -> str:
#     response = llm.invoke([
#         HumanMessage(content=message)
#     ])
#     return response.content


from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="phi3")

def get_response(message: str) -> str:
    return llm.invoke(message)
