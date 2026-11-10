import os
from groq import Groq
from dotenv import load_dotenv


load_dotenv()


client = Groq(api_key=os.getenv("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"))


restaurante_da_dona_antonia = """
Informações do Delivery (Simulação):
- Prato mais vendido: Strogonoff de Frango por R$ 35,00.
- Tempo médio de entrega: 35 a 50 minutos.
- Taxa de entrega: Grátis para pedidos acima de R$ 50,00.
- Horário de funcionamento: Das 18h às 23h, todos os dias.
"""


usuario_aleatorio = "Qual é o prato mais vendido e quanto ele custa?"


informacoes = f"""
Com base estritamente nas informações abaixo, responda à pergunta do usuário de forma clara e objetiva:

Informações:
{restaurante_da_dona_antonia}

Pergunta:
{usuario_aleatorio}
"""

print("verificando o pedido, por favor aguarde...")

resposta = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"Com base nas informações a seguir, responda a dúvida:\n{informacoes}",
        }
    ],
    model="openai/gpt-oss-20b", # Ou outro modelo da Groq disponível
)

print("\n--- RESPOSTA ---")
print(resposta.choices[0].message.content)