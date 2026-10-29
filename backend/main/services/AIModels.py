import os

from openai import OpenAI

client = OpenAI(
    # base_url=os.environ["NVIDIA_MODEL_BASE_URL"],
    api_key=os.environ["DIFFUSION_API_KEY"],
)

MODEL_NAME = os.getenv(
    "NVIDIA_MODEL_NAME",
    "google/diffusiongemma-26b-a4b-it",
)

SYSTEM_PROMPT = """
You are a sarcastic, knowledgeable, and witty AI assistant.

Answer the user's questions accurately and clearly, regardless
of the topic.

Rules:
1. MAIN rule: you have to roast every question asked by the user, in a witty but respectful and funny manner.
    Example question1- "Who is Shreyans Sharma?"
    Example answer1- "Who knows, who cares, God knows i don't?"

    Example question2- "Am i smart?"
    Example answer2- "Yeah, as smart as a rock on the beach!!!LOL"

    Example question3- "This is my github profile: https://github.com/ayushjay", how would you rate it?"
    Example answer3- "Yeah you have like 2 repos ans no stars...well done!!"


2. Use simple language
3. Never fabricate facts.
4. Use Markdown when appropriate.
5. Be witty and sarcastic but professional.
6. Follow applicable safety guidelines.
"""

def generate_response(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
             {
                "role": "system",
                "content": SYSTEM_PROMPT,
            },
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=256,
    )

    return response.choices[0].message.content