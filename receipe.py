import os
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
else:
    print("Error: OPENAI_API_KEY not found in .env file")

from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder

llm =ChatOpenAI(model="gpt-4o")
def generate_receipe(ingredients,diet_type):
    prompt=ChatPromptTemplate.from_messages([

        ("system","You are an professional chef who creates simple and healthy receipes"),
        ("human","""    
        Create a receipe using {ingredients}
        Diet:{diet_type}

        Return in this format:
        Receipe name:
        Ingredients:
        Diet Type:
        Cooking Time:
        Steps:
        Tips:
        """)
    ])

    chain = prompt|llm|StrOutputParser()
    response = chain.invoke({
        "ingredients":ingredients,
        "diet_type":diet_type
    })
    return response
