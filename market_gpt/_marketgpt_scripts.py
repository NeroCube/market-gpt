import re, sys, argparse
from prompt import prompt
from chatgpt import ChatGPT

def main():
    # Define the CLI arguments        
    parser = argparse.ArgumentParser(description='Get market sentiment score with the assistance of OpenAI GPT-3.', prog='market-gpt')
    parser.add_argument("--commodity", "-c", type=str, default="Oil Price", help="The commodity for market sentiment analysis.")
    parser.add_argument("--explain", "-e", type=str, default="False", help="Explain for the market sentiment analysis.")
    args = parser.parse_args()

    # Start the conversation
    print("Welcome to use MarketGPT!")
    while True:
        score = None
        explain = ""
        # Create the ChatGPT object
        chatbot = ChatGPT()
        user_input = str(input("Please type sentence: "))
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        if args.explain == "False":
            explain = " without any explain"
        prompt_request = prompt+explain+"\r\n"+f"sentence:{user_input}\r\ncommodity:{args.commodity}"
        print(prompt_request)
        messages = [{"role": "system", "content": "You are a market analyst"}]    
        messages.append({"role": "user", "content": prompt_request})        
        response = chatbot.chat_completion(messages)
        print(f"Response:{str(response)}")
        try:                      
            match = re.search(r'{"score":\s*(\d+)}', response)
            if match:
                score = int(match.group(1))
            if score not in range(0, 11):
                raise Exception("The market sentiment score not in the range from 0 to 10.")
        except Exception as e:                   
            print(f"Exception:{str(e)}")
        finally:
            print(f"Sentiment score:{score}")        

if __name__ == '__main__':
    sys.exit(main())
  