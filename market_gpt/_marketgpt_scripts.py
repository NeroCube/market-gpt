import sys, json, argparse
from prompt import prompt
from chatgpt import ChatGPT

def main():
    # Define the CLI arguments        
    parser = argparse.ArgumentParser(description='Get market sentiment score with the assistance of OpenAI GPT-3.', prog='market-gpt')
    parser.add_argument("--commodity", "-c", type=str, default="Oil Price", help="The commodity for market sentiment analysis.")
    args = parser.parse_args()

    # Start the conversation
    print("Welcome to use MarketGPT!")
    while True:
        score = None
        # Create the ChatGPT object
        chatbot = ChatGPT()
        user_input = str(input("Please type sentence: "))
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        user_input = prompt+"\r\n"+f"sentence={user_input}\r\ncommodity={args.commodity}"
        response = chatbot.chat(user_input)
        print(f"Response:{str(response)}")
        try:                      
            content = json.loads(str(response))
            score = int(content["score"])
            if score not in range(0, 11):
                raise Exception("The market sentiment score not in the range from 0 to 10.")
        except Exception as e:                   
            print(f"Exception:{str(e)}")
        finally:
            print(f"Sentiment score:{score}")        

if __name__ == '__main__':
    sys.exit(main())
  