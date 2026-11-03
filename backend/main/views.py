import json
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .forms import UserInputForm
from .services.AIModels2 import generate_response_diffusion


def index_view(request):
    contextform = {}
    contextform["form"] = UserInputForm()

    if request.method == "POST":
        contextform = UserInputForm(request.POST)
        if contextform.is_valid():
            # context_dict = {}
            raw_abc = generate_response_diffusion(contextform.cleaned_data['user_prompt'])
            # raw_data = json.loads(raw_abc.content)
            my_result = raw_abc["choices"][0]["message"]["content"]
           
            return render(request, 
                            "main/result.html",
                            {"my_result": my_result})
        
        


    return render(request, "main/index.html", contextform)


# def ask_ai(request):
#     prompt = request.POST.get("prompt", "").strip()

#     if not prompt:
#         return JsonResponse(
#             {"error": "Prompt is required"},
#             status=400,
#         )

#     answer = generate_response(prompt)

#     return JsonResponse({
#             "answer": answer,
#         })

# def result(request):
#     context = ask_ai(request)
#     return render(request, 
#                   "main/result.html",
#                   {"context": context})

