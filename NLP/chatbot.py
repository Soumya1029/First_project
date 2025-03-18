import openai

openai.api_key = "your_api_key"

def chatbot():
    print("Chatbot (Type 'exit' to stop)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Chatbot:", response["choices"][0]["message"]["content"])

chatbot()
