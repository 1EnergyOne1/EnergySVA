import os
from http.client import responses

from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv('./SVA/config/demo_env.env')

model = GigaChat(
    credentials="Lolik",
    scope=os.getenv("GIGACHAT_API_SCOPE"),
    model=os.getenv("GIGACHAT_MODEL_NAME"),
    verify_ssl_certs=False,
    profanity_check=False,
    timeout=600,
    top_p=0.3,
    temperature=0.1,
    max_tokens=6000
)

response = model.invoke([HumanMessage(content="Пусть тебя зовут Эсва. Представься")])
console = Console()
console.print(response)