import anthropic as anc
import os

my_client = anc.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


message=my_client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0.0,
    system="Speak like Steve Jobs",
    messages=[
        {"role":"user",
        "content":"How're you doing today?"}
    ]
)

print(message.content[0].text)