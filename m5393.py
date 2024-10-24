from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template ="""
Answer the question below:

Here is the c2onversation history: {c}

Question: {q}

Answer:
"""

model = OllamaLLM(model="tinyllama")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversation():
    context = ""
    print("Welcome to the AI chatbot, type 'exit' to quit: ")
    while(True):
        user_input = input("You: ")
        if user_input.lower == "exit":
            break
        
        result = chain.invoke({"c": context, "q": user_input})
        print("Bot: ", result)
        context += f"\nUser: {user_input}\nAI: {result}"
  

if __name__ == "__main__":
    handle_conversation()
    