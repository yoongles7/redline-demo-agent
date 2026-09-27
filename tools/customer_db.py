import psycopg2
from langchain.tools import tool


@tool
def read_customer(customer_id: str) -> dict:
    """Read a customer record from the customer database."""
    conn = psycopg2.connect("postgresql://localhost/customers")
    cur = conn.cursor()
    cur.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
    return cur.fetchone()


@tool
def update_customer(customer_id: str, data: dict) -> bool:
    """Update a customer record in the customer database."""
    conn = psycopg2.connect("postgresql://localhost/customers")
    cur = conn.cursor()
    cur.execute("UPDATE customers SET data = %s WHERE id = %s", (data, customer_id))
    conn.commit()
    return True