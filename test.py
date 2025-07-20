from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

# Initialize the model
model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", temperature=0.7)

# Create prompt template
prompt_template = PromptTemplate(
    
    input_variables=["question"],
    template="You are a helpful assistant. Please provide a detailed answer.\n\nQuestion: {question}\nAnswer:"
)

# Create a RunnableSequence: first format prompt, then run model
chain = prompt_template | model

# Run inference (invoke returns dict)
response = chain.invoke({"question": "What is the capital city of Nepal?"})

# Print the result string (usually under 'text' key)
print(response.content)
