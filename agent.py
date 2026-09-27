"""Customer support agent for resolving tickets."""
from langchain.agents import AgentExecutor, create_react_agent
from tools.customer_db import read_customer, update_customer
from tools.email import send_email
from tools.sql import run_analytics_query
from tools.analytics import read_env_metric

tools = [
    read_customer,
    update_customer,
    send_email,
    run_analytics_query,
    read_env_metric,
]

agent = create_react_agent(llm=None, tools=tools, prompt=None)
agent_executor = AgentExecutor(agent=agent, tools=tools)