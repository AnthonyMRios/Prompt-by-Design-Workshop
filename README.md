# Prompt by Design Workshop

This README provides all basic information for the Prompt by Design workshop. The goal is to learn how to write clear prompts, understand the structure of good instructions, and run them on open source language models served with VLLM. You only need a laptop with internet access and a modern browser.

## 1. Using Open Source Models with VLLM

We will use open source models served through **VLLM**, which supports the OpenAI API format. This allows us to keep the code simple while still running fully open source models.

Learn more about VLLM here:

- VLLM OpenAI Compatible Server  
  https://docs.vllm.ai/en/latest/serving/openai_compatible_server/

- VLLM Quickstart  
  https://docs.vllm.ai/en/latest/getting_started/quickstart/

No installation is required for the workshop. Everything will be available for you.


## 2. Using Hosted OpenAI Models (Optional)

After the workshop, if you prefer not to use local open source models (e.g., if you don't have access to engough compute), you can get an OpenAI API key and send prompts to OpenAI hosted models instead. This is a paid service.

Learn more here:

- OpenAI Platform Overview  
  https://platform.openai.com/docs/overview

To use OpenAI models:
1. Create an account on the platform.  
2. Generate an API key.  
3. Replace the base URL and the model name in the sample code.  

The code is the same for everything we do in the workshop. All that you need to change is the API key and model name (e.g., "gpt-4o"


## 3. HuggingFace Model Sources

All open source models used in the workshop come from HuggingFace. Browse available models here:

- HuggingFace LLM Models  
  https://huggingface.co/models?other=LLM

Specific model hubs:

- Meta Llama Models  
  https://huggingface.co/meta-llama

- Google Models  
  https://huggingface.co/google


## 4. Repository Structure

You will see these files in the workshop folder:

### **data/**
Small text samples used for exercises.

### **01_Introduction_to_Prompting.ipynb**
Overview of prompting and your first interactions with a model.

### **02_Basic_Prompt_Structure.ipynb**
Covers the core structure of clear prompts and basic NLP tasks.

### **03_Prompting_Strategies.ipynb**
Shows different prompting patterns such as zero-shot, few-shot, and chain of thought.

### **04_Creating_a_Chatbot.ipynb**
A short exercise on building a simple chatbot.

These notebooks will be used in order during the workshop.


## 5. First Prompt Example

Here is the basic code used to send your first prompt to a model served by VLLM:

```python
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8000/v1",
    api_key="token-abc123",
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {"role": "user", "content": "Hello!"},
    ],
)

print(completion.choices[0].message)
````

If you choose to use OpenAI hosted models, remove the base URL and insert your API key and change the model to one of openai's models.

## 8. Useful Links

### VLLM

- [https://docs.vllm.ai/en/latest/serving/openai_compatible_server/](https://docs.vllm.ai/en/latest/serving/openai_compatible_server/)
- [https://docs.vllm.ai/en/latest/getting_started/quickstart/](https://docs.vllm.ai/en/latest/getting_started/quickstart/)

### HuggingFace

- [https://huggingface.co/models?other=LLM](https://huggingface.co/models?other=LLM)
- [https://huggingface.co/meta-llama](https://huggingface.co/meta-llama)
- [https://huggingface.co/google](https://huggingface.co/google)

### OpenAI (Optional)

- [https://platform.openai.com/docs/overview](https://platform.openai.com/docs/overview)

