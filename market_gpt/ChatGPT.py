import openai

class ChatGPT:
    def __init__(self, api_key, model_engine="text-davinci-003"):
        openai.api_key = api_key
        self.model_engine = model_engine

    def chat(self, prompt, temperature=0.5, max_tokens=50, stop="\n\n", top_p=1, frequency_penalty=0.3, presence_penalty=0.3):
        response = openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            stop=stop,
            top_p=top_p,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty
        )
        if not response.choices:
            raise Exception("GPT could not generate a response.")
        return response.choices[0].text.strip()