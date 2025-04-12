import google.generativeai as genai
from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image  # Import Pillow library

genai.configure(api_key=settings.GOOGLE_API_KEY)

def chat_view(request):
    response_text = ""
    if request.method == "POST":
        user_message = request.POST.get("user_message")
        image = request.FILES.get('image')

        try:
            model = genai.GenerativeModel('gemini-2.0-flash') #Change model
            if image:
                # Process the image
                img = Image.open(image)
                response = model.generate_content([user_message, img]) #Pass image to model
                response_text = response.text
            else:
                response = model.generate_content(user_message)
                response_text = response.text
        except Exception as e:
            response_text = f"Error: {e}"

    return render(request, "home.html", {"response": response_text})