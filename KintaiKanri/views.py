from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import MPjKnr
from .forms import KintaiForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class KintaiNyuryoku(CreateView):
    model = MPjKnr
    form_class = KintaiForm
    
