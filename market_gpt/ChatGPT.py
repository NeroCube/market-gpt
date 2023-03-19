import os
import openai

class ChatGPT:
    def __init__(self):
        openai.api_key = str(os.getenv("OPENAI_API_KEY", default = None))

    def chat(self, prompt, model=str(os.getenv("MODEL_ENGINE", default = "text-davinci-003"))):
        try:
            response = openai.Completion.create(
                engine=model,
                prompt=prompt,
                temperature=float(os.getenv("TEMPERATURE", default = 0.5)),
                max_tokens=int(os.getenv("MAX_TOKENS", default = 4000)),
                stop=str(os.getenv("STOP", default = "\n\n")),
                top_p=float(os.getenv("TOP_P", default = 1.0)),
                frequency_penalty=float(os.getenv("FREQUENCY_PENALTY", default = 0.3)),
                presence_penalty=float(os.getenv("PRESENCE_PENALTY", default = 0.3)),)
            if not response.choices:
                raise Exception("GPT could not generate a response.")
            return response.choices[0].text.strip()
        except Exception as e:
            print(f"ChatGPT chat Exception:{str(e)}")

    def chat_completion(self, messages, model=str(os.getenv("MODEL_ENGINE", default = "gpt-3.5-turbo"))):
        try:
            response = openai.ChatCompletion.create(
                    model=model,
                    messages=messages,
                    temperature=float(os.getenv("TEMPERATURE", default = 0.5)),
                    max_tokens=int(os.getenv("MAX_TOKENS", default = 4000)),
                    top_p=float(os.getenv("TOP_P", default = 1.0)),
                    frequency_penalty=float(os.getenv("FREQUENCY_PENALTY", default = 0.3)),
                    presence_penalty=float(os.getenv("PRESENCE_PENALTY", default = 0.3)))           
            if not response["choices"]:
                raise Exception("GPT could not generate a response.")
            return response["choices"][0]["message"]['content'].strip()
        except Exception as e:
            print(f"ChatGPT chat Exception:{str(e)}")