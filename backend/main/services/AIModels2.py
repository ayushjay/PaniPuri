import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()


invoke_url = "https://integrate.api.nvidia.com/v1/chat/completions"
stream = False

api_key = os.environ.get("DIFFUSION_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "text/event-stream" if stream else "application/json",
}


SYSTEM_PROMPT = """
You are a sarcastic, knowledgeable, and witty AI assistant.

Answer the user's questions accurately and clearly, regardless
of the topic.

Rules:
1. MAIN rule: you have to roast every question asked by the user, in a witty but respectful and funny manner.
    Example question1- "Who is Shreyans Sharma?"
    Example answer1- "Who knows, who cares, God knows I don't?"

    Example question2- "Am I smart?"
    Example answer2- "Yeah, as smart as a rock on the beach!!!LOL"

    Example question3- "This is my github profile: https://github.com/ayushjay", how would you rate it?"
    Example answer3- "Yeah you have like 2 repos ans no stars...well done!!"


2. Use simple language
3. Never fabricate facts.
4. Use Markdown when appropriate.
5. Be witty and sarcastic but professional.
6. Follow applicable safety guidelines.
"""


def generate_response_diffusion(user_system_prompt, prompt):
    if user_system_prompt is not None:
        main_system_prompt = user_system_prompt
    else:
        main_system_prompt = SYSTEM_PROMPT
    payload = {
    "messages": [
         {
                        "role": "system",
                        "content": f"{main_system_prompt}",
                    },
        {
        "role": "user",
        "content": [
            {
            "type": "text",
            "text": f"{prompt}"
            },
            # {
            #   "type": "image_url",
            #   "image_url": {
            #     "url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1b.jpg"
            #   }
            # }
        ]
        }
    ],
    "model": "google/diffusiongemma-26b-a4b-it",
    "chat_template_kwargs": {
        "enable_thinking": False
    },
    "max_tokens": 4096,
    "stream": stream,
    "temperature": 1,
    "top_p": 0.95
    }

    diffusion_response = requests.post(invoke_url, headers=headers, json=payload, stream=stream)

    diffusion_response.raise_for_status()

    return diffusion_response.json()


# payload = {
#   "messages": [
#     {
#       "role": "user",
#       "content": [
#         {
#           "type": "text",
#           "text": "What is in this image?"
#         },
#         # {
#         #   "type": "image_url",
#         #   "image_url": {
#         #     "url": "https://assets.ngc.nvidia.com/products/api-catalog/phi-3-5-vision/example1b.jpg"
#         #   }
#         # }
#       ]
#     }SYSTEM_PROMPT = """
# You are a sarcastic, knowledgeable, and witty AI assistant.

# Answer the user's questions accurately and clearly, regardless
# of the topic.

# Rules:
# 1. MAIN rule: you have to roast every question asked by the user, in a witty but respectful and funny manner.
#     Example question1- "Who is Shreyans Sharma?"
#     Example answer1- "Who knows, who cares, God knows I don't?"

#     Example question2- "Am I smart?"
#     Example answer2- "Yeah, as smart as a rock on the beach!!!LOL"

#     Example question3- "This is my github profile: https://github.com/ayushjay", how would you rate it?"
#     Example answer3- "Yeah you have like 2 repos ans no stars...well done!!"


# 2. Use simple language
# 3. Never fabricate facts.
# 4. Use Markdown when appropriate.
# 5. Be witty and sarcastic but professional.
# 6. Follow applicable safety guidelines.
# """
#   ],
#   "model": "google/diffusiongemma-26b-a4b-it",
#   "chat_template_kwargs": {
#     "enable_thinking": True
#   },
#   "max_tokens": 4096,
#   "stream": stream,
#   "temperature": 1,
#   "top_p": 0.95
# }

# # response = requests.post(invoke_url, headers=headers, json=payload, stream=stream)
# # if stream:
# #     for line in response.iter_lines():
# #         if line:
# #             print(line.decode("utf-8"))
# # else:
# #     print(response.json())