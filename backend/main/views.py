from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .services.AIModels import generate_response


@require_POST
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


