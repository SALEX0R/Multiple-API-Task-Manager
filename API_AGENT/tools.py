from langchain.tools import StructuredTool
from langchain.pydantic_v1 import BaseModel, Field

from utils import execute_api




class APIEXETOOL(BaseModel):
    url: str = Field(description="Executes requests to set of prespecified API given in api_endpoint list")
    params: dict = Field(description="consisting of a json body with parameters given by params key in api_endpoint list associated with the url to be sent to POST api") 
    api_type: str = Field(description="can only take one value from the following list [GET, POST, DELETE]") 


apiexetool = StructuredTool.from_function(
    func=execute_api,
    name="API_EXE_TOOL",
    description="Executes requests to set of prespecified API endpoints for managing items.",
    args_schema=APIEXETOOL,
    return_direct=True,
)
