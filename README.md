import logging
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.agents import Tool, AgentExecutor
from app.tools.product_tools import ProductUploadTool, ProductSearchTool
from app.tools.order_tools import OrderPlacementTool
from app.tools.calendar_tools import CreateMeetingTool, GetMeetingTool
from app.tools.expense_tools import AddExpenseTool, ExpenseReportTool, ExpenseAnalysisTool

# Logging setup
logging.basicConfig(level=logging.INFO)

# Initialize Langchain tools
tools = [
    ProductUploadTool(),
    ProductSearchTool(),
    OrderPlacementTool(),
    CreateMeetingTool(),
    GetMeetingTool(),
    AddExpenseTool(),
    ExpenseReportTool(),
    ExpenseAnalysisTool()
]

# Initialize LLM model (Here we use OpenAI, but you can replace it with llama3 or others as needed)
llm = OpenAI(model="llama3-groq-70b-8192-tool-use-preview")

# Define the prompt template for reasoning with the agent
prompt_template = """
You are a helpful assistant capable of interacting with several APIs. Here's what you can do:
1. Upload products
2. Search products
3. Place orders
4. Create meetings
5. Get meetings
6. Add expenses
7. Get expense reports (in CSV format)
8. Get expense analysis (in PDF format)

Based on the user's query, determine the appropriate action and provide the required information. The available tools are: {tools}.

User Query: {query}
"""

# Set up Langchain agent and LLM chain
prompt = PromptTemplate(input_variables=["query", "tools"], template=prompt_template)
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Initialize the agent with the tools and LLM chain
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Initialize the AgentExecutor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Function to get the agent executor instance
async def get_agent_executor():
    return agent_executor


Example Request:
json
Copy code
{
  "query": "Upload a product called 'Smartphone' costing 300 dollars with a description 'Latest 5G model'."
}
Example Response:
json
Copy code
{
  "response": {"status": "success", "message": "Product uploaded successfully"}
}
This code structure handles multiple types of queries (product upload, meeting creation, expense reports) with agent logic, allowing you to customize and extend it further as per your needs.
