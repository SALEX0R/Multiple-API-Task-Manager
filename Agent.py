from langchain.chat_models import ChatOpenAI
from tools import apiexetool
from langchain.agents import AgentExecutor
from langchain.agents import AgentExecutor, create_structured_chat_agent
from api_endpoint import api_endpoint_task_manager
from prompt import prompt_template
from langchain.prompts import PromptTemplate

llm = ChatOpenAI(model="gpt-4", temperature=0, openai_api_key="OpenAI_API_KEY_HERE")

# multi shot learning example with agent

examples = '''
Example 1:

user_query: get me information of task 2
Thought: To get the details of the task with item id's, I need to use the GET method on the first API endpoint and replace the url parameter with provided item_id. The item_id after replacement in the URL will yield http://127.0.0.1:5000/items/2.

Action: API_EXE_TOOL
Action Input: {"url": "http://127.0.0.1:5000/items/2","params":{}, "api_type": "GET"}

Example 2:

user_query: I have completed task 1
Thought: To remove the item from the task list, I need to use the DELETE method on the third API endpoint and replace the url parameter with provided item_id. The item_id after replacement in the URL will yield http://127.0.0.1:5000/items/1.

Action: API_EXE_TOOL
Action Input: {"url": "http://127.0.0.1:5000/items/2","params":{}, "api_type": "DELETE"}

Example 3:

user_query: I have completed task 1
Thought: please schedule a meeting with Yahiko at 2:30pm tommorow.

Action: API_EXE_TOOL
Action Input: {"url": "http://127.0.0.1:5000/items","params": {
            "name": "Schedule a meeting",
            "description": "a meeting with Yahiko at 2:30pm tommorow"
        }, "api_type": "POST"}

'''

prompt = """
You are an agent which keeps a list of task and manages it, you can either add task, view task with item id or delete a task. Perform relevant actions based on user query.  

Answer the question as best as you can using the following tool: 


api_endpoints = [{api_endpoints}]

please refer to examples below to understand the tool call:
{examples}

"""+prompt_template
prompt = PromptTemplate(
    input_variables=['agent_scratchpad', 'input', 'tool_names', 'tools',],
    template=prompt,
    partial_variables={"api_endpoints":api_endpoint_task_manager, "examples":examples }
    
)

tools = [apiexetool]

agent = create_structured_chat_agent(llm, tools, prompt)
# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(
    agent=agent, tools=tools, verbose=True, handle_parsing_errors=True
)
print(agent_executor.invoke({"input": "I have completed the task 2 "}))
