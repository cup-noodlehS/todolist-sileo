# from django.shortcuts import render, HttpResponse, HttpResponseRedirect
# from django.urls import reverse
# import json
# from django.views.decorators.csrf import csrf_exempt
# from django.http import JsonResponse
# from .models import Item
# from asgiref.sync import sync_to_async


# def index(request):
#     items = Item.objects.all().order_by("-pub_date")
#     item_list = [{"pk": item.pk,"text": item.text, "pub_date": item.pub_date, "completed":item.completed} for item in items]
#     return JsonResponse({"items": item_list})

# @csrf_exempt
# def create(request):
#     if request.method == "POST":
#         data = json.loads(request.body)

#         i = Item(text=data["text"])
#         i.save()
        
#         return HttpResponseRedirect(reverse('todoapp:index'))

#     return JsonResponse({'error': 'Invalid request'}, status=400)

# @csrf_exempt
# def update(request):
#     if request.method == "PUT":
#         data = json.loads(request.body)
#         i = Item.objects.get(pk=data["pk"])
#         i.text = data["text"]
#         i.completed = data["completed"]
#         i.save()
        
#         return JsonResponse({'message': 'Item updated successfully'})

#     return JsonResponse({'error': 'Invalid request'}, status=400)

# @csrf_exempt
# def delete(request, id):
#     if request.method == 'DELETE':
#         print("IDDD!!!" + str(id))
#         item = Item.objects.get(pk=id)
#         print(item.text)
#         item.delete()

#         return JsonResponse({'message': 'Item updated deleted'})
    
#     return JsonResponse({'error': 'Invalid request'}, status=400)