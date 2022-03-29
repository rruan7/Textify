from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)

# Create your views here.

from rest_framework import viewsets
from .serializers import TextifySerializer
from .models import Textify
from .forms import TextifyForm

from .TextDetector import getText

# Create your views here.

class TextifyView(viewsets.ModelViewSet):
    def textify_view(request):
        # queryset: returns a collection of all Set objects
        textifys = Textify.objects.all()
        for textify in textifys:
            # extract text
            extracted_text = getText(textify.image)
            # result string
            text = ""
            # update result string
            for word in extracted_text:
                text += str(word.description)
                text += " "
            # print(text)
            # update database
            textify.text = text
            textify.save()
        # context dictionary: used to send information to template
        context = {
            'textifys': Textify.objects.all(),
        }
        return render(request, 'textify_view.html', context)
    
    def update_textify(request, id):
        # dictionary for initial data with
        # field names as keys
        context ={}
    
        # fetch the object related to passed id
        obj = get_object_or_404(Textify, id = id)
    
        # pass the object as instance in form
        form = TextifyForm(request.POST or None, instance = obj)
    
        # save the data from the form and
        # redirect to default view
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    
        # add form dictionary to context
        context["form"] = form
    
        return render(request, "update_textify.html", context)