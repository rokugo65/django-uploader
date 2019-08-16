from django.shortcuts import render
from django.views.generic import TemplateView

from uploader.forms import ImageForm

class TopView(TemplateView):
    template_name = "top.html"

    def get(self, request, *args, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        form = ImageForm()
        context['form'] = form
        return render(self.request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = super(TopView, self).get_context_data(**kwargs)
        form = ImageForm(request.POST, request.FILES)
        
        if form.is_valid():
            context['filename'] = str(request.FILES['image'])
            form.save()

        form = ImageForm()
        context['form'] = form
        return render(self.request, self.template_name, context)
