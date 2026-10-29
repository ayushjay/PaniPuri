from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .services.AIModels import generate_response


def index_view(request):
    return render(request, "main/index.html")


def ask_ai(request):
    prompt = request.POST.get("prompt", "").strip()

    if not prompt:
        return JsonResponse(
            {"error": "Prompt is required"},
            status=400,
        )

    answer = generate_response(prompt)

    return JsonResponse({
            "answer": answer,
        })

def result(request):
    context = ask_ai(request)
    return render(request, 
                  "main/result.html",
                  {"context": context})

