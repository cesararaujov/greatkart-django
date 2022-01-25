from .models import Cateogory

def menu_links(request):
        links   =   Cateogory.objects.all()
        return dict(links=links)
