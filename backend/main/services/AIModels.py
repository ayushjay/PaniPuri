import os

from openai import OpenAI

client = OpenAI(
    base_url=os.environ["NVIDIA_MODEL_BASE_URL"],
    api_key=os.environ["DIFFUSION_API_KEY"],
)

MODEL_NAME = os.getenv(
    "NVIDIA_MODEL_NAME",
    "google/diffusiongemma-26b-a4b-it",
)


def generate_response(prompt):
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=256,
    )

    return response.choices[0].message.content