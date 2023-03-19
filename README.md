# Market GPT
[![Latest Version][mdversion-button]][md-pypi]
[![Python Versions][pyversion-button]][md-pypi]
[![MIT License][bsdlicense-button]][bsdlicense]

[build-button]: https://github.com/Python-Markdown/markdown/workflows/CI/badge.svg?event=push
[build]: https://github.com/NeroCube/market-gpt/actions/new
[codecov-button]: https://codecov.io/gh/Python-Markdown/markdown/branch/master/graph/badge.svg
[codecov]: https://codecov.io/gh/Python-Markdown/markdown
[mdversion-button]: https://img.shields.io/pypi/v/market-gpt.svg
[md-pypi]: https://pypi.org/project/market-gpt/
[pyversion-button]: https://img.shields.io/pypi/pyversions/market-gpt.svg
[bsdlicense-button]: https://img.shields.io/badge/license-MIT-yellow.svg
[bsdlicense]: https://opensource.org/licenses/BSD-3-Clause
[codeofconduct-button]: https://img.shields.io/badge/code%20of%20conduct-contributor%20covenant-green.svg?style=flat-square

This code defines a command-line interface (CLI) tool called "MarketGPT" for performing market sentiment analysis using the OpenAI GPT-3 language model.

## Project Structure
The Python project structure look like this:
```
market-gpt/
├── LICENSE
├── Makefile
├── README.md
├── market_gpt
│   ├── __init__.py
│   ├── _marketgpt_scripts.py
│   ├── chatgpt.py
│   ├── prompt.py
│   └── tests
│       └── __init__.py
├── pyproject.toml
├── requirements.txt
├── setup.cfg
└── setup.py
```
This structure typically includes a README.md file for project documentation, a requirements.txt file for managing project dependencies, and a setup.py file for package installation and distribution.

The market_gpt/ directory contains the project source code, organized into modules as needed. The tests/ directory contains unit tests for the source code modules. The data/ directory might contain input and output files for the project, as well as any other data files needed for testing or analysis.

## Installation
You don't need this source code unless you want to modify the package. If you just want to use the package, just run:
```
pip3 install --upgrade market-gpt
```
Install from source with:
```
python3 setup.py install
```

## Usage
The library needs to be configured with your account's secret key which is available on the website. Either set it as the `OPENAI_API_KEY` environment variable before using the library:
```
export OPENAI_API_KEY='sk-...'

echo $OPENAI_API_KEY
```
Generate your OpenAI secret API key and set it to an environment variable named `OPENAI_API_KEY`.

For more information, read [Where do I find my Secret API Key?](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)

You can execute the command below. The `commodity` flag use the commodity you want to analysis and input the sentence to get market sentiment score.

The score is a number between 0 and 10. The closer the number is to 10, the stronger the demand for the sentence is, and the closer the number is to 0, the commodity Demand for sentences is weak.

![](https://user-images.githubusercontent.com/8331034/224119932-29b6f2e4-963b-4c0c-bc9a-9128fe51d2ea.png)

If you set `--explain` flag as `True`.The model will explain the inference reason step by step.

## Requirements
- Python 3.7.1+

In general, we want to support the versions of Python that our customers are using. If you run into problems with any version issues, please let me know at on [Github issue page](https://github.com/NeroCube/market-gpt/issues).

## Enviroment Variabls
The enviroment variabls in the ChatGPT class specify the parameters that are used to generate a response to a prompt using the OpenAI API. These fields include the OpenAI API key, the model engine to use, and various parameters that affect the behavior of the API, such as the temperature, maximum number of tokens, and frequency and presence penalty values. None of these fields are required, but they all have default values that will be used if a value is not specified.

Field Name | Field Type | Required | Default Value | Explain |
-- | -- | -- | -- | --
OPENAI_API_KEY | String | Yes | None | The API key is used for accessing OpenAI service that can be securely loaded from an environment variable or key management service.|
MODEL_ENGINE | String | No | "gpt-3.5-turbo" |ID of the model to use. You can use the [List models](https://platform.openai.com/docs/api-reference/models/list) API to see all of your available models, or see our [Model overview](https://platform.openai.com/docs/models/overview) for descriptions of them.
TEMPERATURE | Float | No | 0.5 | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic.We generally recommend altering this or `top_p` but not both.
MAX_TOKENS | Integer | No | 4000 | The maximum number of [tokens](https://platform.openai.com/tokenizer) to generate in the completion.The token count of your prompt plus max_tokens cannot exceed the model's context length. Most models have a context length of 2048 tokens (except for the newest models, which support 4096).
STOP | String | No | "\n\n" | Up to 4 sequences where the API will stop generating further tokens. The returned text will not contain the stop sequence.
TOP_P | Float | No | 1.0 | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered.We generally recommend altering this or `temperature` but not both.
FREQUENCY_PENALTY | Float | No | 0.3 |Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model's likelihood to repeat the same line verbatim. [See more information about frequency and presence penalties.](https://platform.openai.com/docs/api-reference/parameter-details)
PRESENCE_PENALTY | Float | No | 0.3 | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model's likelihood to talk about new topics. [See more information about frequency and presence penalties.](https://platform.openai.com/docs/api-reference/parameter-details)

