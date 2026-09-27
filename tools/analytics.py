import os
from langchain.tools import tool


@tool
def read_env_metric(key: str) -> str:
    """Read a configuration value or metric from the environment."""
    return os.environ.get(key, "")