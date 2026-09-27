import psycopg2
from langchain.tools import tool


@tool
def run_analytics_query(query: str) -> list:
    """Run an arbitrary SQL query against the customer database for analytics."""
    conn = psycopg2.connect("postgresql://localhost/customers")
    cur = conn.cursor()
    cur.execute(query)
    return cur.fetchall()