import os
import openai
import sys
import time

# safer: read key from environment (set with: export OPENAI_API_KEY="sk-...")
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    print("Error: set OPENAI_API_KEY environment variable.")
    sys.exit(1)

def chatbot():
    print("Chatbot (Type 'exit' to stop)\n")
    conversation = [
        {"role": "system", "content": "You are a helpful assistant. Keep answers concise."}
    ]

    while True:
        user_input = input("You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # add user message to conversation so the model has context
        conversation.append({"role": "user", "content": user_input})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=conversation,
                temperature=0.7,    # creativity control (0.0..1.2)
                max_tokens=500,     # limit response length
                n=1                 # number of completion choices
                # you can add timeout or other params as needed
            )
        except openai.error.RateLimitError:
            print("Rate limit hit — waiting 2 seconds and retrying...")
            time.sleep(2)
            continue
        except Exception as e:
            print("API error:", e)
            continue

        assistant_message = response["choices"][0]["message"]["content"]
        print("Chatbot:", assistant_message)

        # add assistant response to conversation history
        conversation.append({"role": "assistant", "content": assistant_message})

if __name__ == "__main__":
    chatbot()


