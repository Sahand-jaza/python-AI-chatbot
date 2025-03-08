import google.generativeai as genai
from django.conf import settings
from django.shortcuts import render

genai.configure(api_key=settings.GOOGLE_API_KEY)

def chat_view(request):
    response_text = ""
    if request.method == "POST":
        user_message = request.POST.get("user_message")
        if user_message:
            try:
                model = genai.GenerativeModel('gemini-2.0-flash')
                response = model.generate_content(user_message)
                response_text = response.text
            except Exception as e:
                response_text = f"Error: {e}"

    return render(request, "home.html", {"response": response_text})