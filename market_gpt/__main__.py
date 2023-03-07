import argparse
from prompt import prompt
from ChatGPT import ChatGPT

def main():
    # Define the CLI arguments        
    parser = argparse.ArgumentParser(description='Get market sentiment score with the assistance of OpenAI GPT-3.', prog='market-gpt')
    parser.add_argument("--api-key", "-k", type=str, required=True, help="OpenAI API key.")
    parser.add_argument("--commodity", "-c", type=str, default="Oil Price", help="The commodity for market sentiment analysis.")
    args = parser.parse_args()

    # Create the ChatGPT object
    chatbot = ChatGPT(api_key=args.api_key)

    # Start the conversation
    print("Welcome to use MarketGPT!")
    while True:
        user_input = str(input("Please type sentence: "))
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        user_input = prompt+"\r\n"+f"sentence={user_input}\r\ncommodity={args.commodity}"
        response = chatbot.chat(user_input)
        print(f"Sentiment Score: {response}")

if __name__ == '__main__':
  main()