# Multiple API Agent Using LangChain and OpenAI

## Overview
 This project demonstrates an intelligent agent that manages tasks through API interactions,
 leveraging LangChain and OpenAI's GPT-4 model. The agent can retrieve, create, and delete tasks based on user queries.

## Features
- **Task Retrieval**: Get details of specific tasks.
- **Task Creation**: Add new tasks with a name and description.
- **Task Deletion**: Remove tasks by their ID.

## Setup and Configuration
## Prerequisites
 - Python 3.10+
 - Flask
 - LangChain
 - OpenAI
 - Requests

## Installation
1. Clone the repository:
   ```
    git clone https://github.com/your-username/multiple-api-agent.git
    cd multiple-api-agent
   ```
2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   ```
   # In Agent.py and Utils.py
   openai_api_key="YOUR_OPENAI_API_KEY"
   ```

# Running the Application
1. Start the Flask server:

```
python App.py

```

2. Run the agent:
```
python Agent.py

```

# Usage
## Example Queries
 - **Retrieve Task**:
    ```
    User: Get me information of task 2

    ```

 - **Create Task**:
   ```
   User: Schedule a meeting with Yahiko at 2:30pm tomorrow

   ```

 - Delete Task:
   ```
   User: I have completed task 1
  
   ```

## API Endpoints
- **GET** /items: Retrieves all tasks.
- **GET** /items/<int:item_id>: Retrieves a specific task by its ID.
- **POST** /items: Creates a new task.
- **DELETE** /items/<int:item_id>: Deletes a specific task by its ID.

## Future Enhancements
- Integrate additional tools or APIs to expand the agent’s functionality.
- Develop a user interface for easier interaction.
- Implement advanced natural language understanding for more complex queries.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Demo

