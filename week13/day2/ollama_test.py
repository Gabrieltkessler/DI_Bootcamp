import requests
import json

def ask(prompt, model='qwen3:0.6b', system=None, temp=0.8, max_token=800):
    if "qwen3" in model:
        prompt += " /no_think"
    r = requests.post(
        "http://127.0.0.1:11434/vi/chat/completions",
        json = {
            "model": model,
            "messages": [{"role":"system", "content":system or ""}, {"role":"user", "content":prompt}],
            "temperature": temp,
            "max_token": max_token
        },
        timeout = 120
    )
    return r.json()["choices"][0]["message"]["content"]

print(ask("how many days in a decade?"))