import os
from rich.console import Console
from langchain_core.messages import HumanMessage
from rich.panel import Panel

from source.agent import model


def run_agent():
    console = Console()

    while True:
        # Запрашиваем у пользователя ввод
        user_input = input("\nЗадай вопрос (или введи 'exit' для выхода): ")

        if user_input.lower() == 'exit':
            break

        try:
            # Отправляем сообщение в модель
            response = model.invoke([HumanMessage(content=user_input)])

            # Отображаем ответ в красивой форме
            panel = Panel.fit(str(response.content), title="Ответ", border_style="green")
            console.print(panel)
        except Exception as e:
            print(f"\nОшибка обработки запроса: {e}")


if __name__ == "__main__":
    run_agent()