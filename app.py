import os
import openai
import dotenv
dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv("API_KEY")

def chat_with_gpt():
    if not OPENAI_API_KEY:
        print("API key is not set. Please set the API key in .env file.")
        return

    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    conversation = []

    print("Console ChatGPT. type 'exit' or 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Terminated.")
            break
        
        conversation.append({"role": "user", "content": user_input})
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=conversation
            )
            bot_reply = response.choices[0].message.content
            print("ChatGPT:", bot_reply)
            
            conversation.append({"role": "assistant", "content": bot_reply})
        
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    chat_with_gpt()
