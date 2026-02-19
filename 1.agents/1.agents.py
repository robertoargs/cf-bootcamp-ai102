# Carly Mamani Chavez Code
# https://ai.azure.com/doc/azure/ai-foundry/agents/quickstart?pivots=ai-foundry-portal&tid=9eaddbdd-d773-411c-a4aa-acab32a45c95

# Libraries and packages
import os
from dotenv import load_dotenv
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.agents.models import CodeInterpreterTool

# Initialize environment variables
load_dotenv()

# Logic to create an agent with the Code Interpreter tool
# print(os.getenv("MICROSOFT_FOUNRDY_ENDPOINT"))

project_client = AIProjectClient(
    endpoint=os.getenv("MICROSOFT_FOUNRDY_ENDPOINT"),
    credential=DefaultAzureCredential()
)

code_interpreter_tool = CodeInterpreterTool()

with project_client:
    agent = project_client.agents.create_agent(
        model=os.getenv("DEPLOYMENT_MODEL"),
        name="my-cf-agent",
        instructions="You are a helpful math teacher that answers questions and solves problems. Use Code Interpreter when seeing numbers.",
        tools=code_interpreter_tool.definitions
    )
print(f"Agent was created with id: {agent.id}")

# Create a thread for communication
thread = project_client.agents.threads.create()
print(f"Created thread, ID: {thread.id}")

question = """Solve the following problem x2 + 5x + 6 = 0. Please show your work."""

# Add a message to the thread
message = project_client.agents.messages.create(
    thread_id=thread.id,
    role="user",  # Role of the message sender
    content=question,  # Message content
)
print(f"Created message, ID: {message.id}")

# Create and process an agent run
run = project_client.agents.runs.create_and_process(
    thread_id=thread.id,
    agent_id=agent.id,
    additional_instructions="""Please the user name's is Cody, talk to him in a friendly manner and make sure to use the Code Interpreter tool to solve the problem."""
)

print(f"Run finished with status: {run.status}")

# Check if the run failed
if run.status == "failed":
    print(f"Run failed: {run.last_error}")

# Fetch and log all messages
messages = project_client.agents.messages.list(thread_id=thread.id)
print(f"Messages: {messages}")

for message in messages:
    print(f"Role: {message.role}, Content: {message.content}")
    # for this_content in message.content:
    #     print(f"Content Type: {this_content.type}, Content Data: {this_content}")
    #     if this_content.text.annotations:
    #         for annotation in this_content.text.annotations:
    #             print(f"Annotation Type: {annotation.type}, Text: {annotation.text}")
    #             print(f"Start Index: {annotation.start_index}")
    #             print(f"End Index: {annotation.end_index}")
    #             print(f"File ID: {annotation.file_path.file_id}")
                # Save every image file in the message
                # file_id = annotation.file_path.file_id
                # file_name = f"{file_id}_image_file.png"
                # project_client.agents.files.save(file_id=file_id, file_name=file_name)
                # print(f"Saved image file to: {Path.cwd() / file_name}")
#Uncomment these lines to delete the agent when done
#project_client.agents.delete_agent(agent.id)
#print("Deleted agent")

# Final Class Notes
# 1. You can do the same with MCP (search for MCP in the documentation) to create agents that can 
# search the web for information.
# 2. I can install extension on VSCode and Azure AI Foundry
# 3. Guardrails + Controls: Content Filters. Injection Prompt.