'''from django.http import JsonResponse

def home_view(request):
    return JsonResponse({'message': 'Bem-vindo ao sistema de cadastro de alunos!'})'''

from django.views import View
from django.http import JsonResponse

class HomeView(View):
    def get(self, request):
        return JsonResponse({'message': 'Bem-vindo ao sistema de cadastro de alunos!'})
