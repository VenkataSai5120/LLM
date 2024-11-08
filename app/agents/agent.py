from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from app.tools.product_tools import ProductUploadTool
from app.tools.meeting_tools import MeetingCreateTool
from app.tools.expense_tools import ExpenseReportTool

# Initialize the tools
tools = [
    ProductUploadTool(),
    MeetingCreateTool(),
    ExpenseReportTool()
]

# Define the prompt template
prompt_template = """
You are an intelligent assistant capable of interacting with multiple APIs. Below are the actions you can perform and the required fields for each:
1. **Upload Product**: You need the following fields: product_name, product_cost, product_description
2. **Search Product**: You need either product_name OR product_description
3. **Place Order**: You need product_id
4. **Create Meeting**: You need meeting_name, user_id, start_time, end_time
5. **Add Expense**: You need user_id, order_id, expense_amount, category
6. **Expense Report**: You need user_id
7. **Expense Analysis**: You need user_id

User Query: {query}
"""

# Initialize Langchain LLM
llm = OpenAI(model="gpt-3.5-turbo")

# Define the LLMChain
llm_chain = LLMChain(prompt=prompt_template, llm=llm)

# Initialize Langchain Agent
agent = initialize_agent(
    tools, llm, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Function to handle user queries
def process_query(query: str):
    result = agent.run(query)
    return result
