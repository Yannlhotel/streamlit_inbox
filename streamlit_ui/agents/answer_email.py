from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="deepseek-r1:1.5b")

def generate_email_reply(email_body: str, answer_desired : str) -> str:
    prompt = f"""
You are a helpful assistant that replies to emails professionally and politely.

Email received:
\"\"\"{email_body}\"\"\"

Know make the reply according to these following informations:
My name is Yann L'HOTELIER
Add the information that : {answer_desired}
"""
    # Correct method call
    response = llm.invoke(prompt)
    return response

if __name__ == "__main__":
    example_email = """Hi team,

Can we move the meeting to Thursday afternoon.

Best,
Alice"""
    answer_desired = "I can't be there Thursday so we don't move the meeting"
    reply = generate_email_reply(example_email,answer_desired)
    print("=== Generated Reply ===")
    print(reply)