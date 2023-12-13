from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import requests
from google.cloud import vision

@csrf_exempt
def generate_product_description(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        
        # Call OpenAI GPT-3 API for text completion
        gpt_response = requests.post('https://api.openai.com/v1/engines/davinci-codex/completions', json={'prompt': f'Generate a product description for a {title}'})

        description = gpt_response.json()['choices'][0]['text']

        # Extract keywords for SEO
        # This is a simplified example, you might want to use a proper NLP library for better keyword extraction
        keywords = description.split()[:5]

        return JsonResponse({'description': description, 'keywords': keywords})

@csrf_exempt
def image_recognition(request):
    if request.method == 'POST':
        image = request.FILES.get('image', None)

        if image:
            # Use Google Cloud Vision API for image recognition
            client = vision.ImageAnnotatorClient()
            content = image.read()
            image = vision.Image(content=content)

            response = client.label_detection(image=image)
            keywords = [label.description for label in response.label_annotations]

            return JsonResponse({'keywords': keywords})

    return JsonResponse({'error': 'Invalid request'})
