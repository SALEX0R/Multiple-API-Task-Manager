#import mysql.connector
from langchain_openai import ChatOpenAI
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate

import requests

llm = ChatOpenAI(
    model="gpt-3.5-turbo-0613",
    openai_api_key="OpenAI_API_KEY_HERE",
)


class apiCall(BaseModel):
    output: str = Field(description="API should pass the parameter")




import requests

def execute_api(url, params=None, api_type=None):
    try:
        if api_type is None:
            raise ValueError("API type must be specified")

        # Switch case for different API types
        if api_type == 'GET':
            response = requests.get(url, params=params)
        elif api_type == 'DELETE':
            response = requests.delete(url, params=params)
        elif api_type == 'POST':
            response = requests.post(url, data=params)  # Assuming params are data for POST request
        else:
            raise ValueError("Unsupported API type")

        response.raise_for_status()

        return {"url_called": url, "response": response.json(), "status": response.status_code}
    except Exception as error:
        print("Error executing the API:", error)
        return None
