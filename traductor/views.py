from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from traductor.forms import TraductorForm
from googletrans import Translator

translator = Translator()
# def translate(text):
#     print(translator.translate(text, dest='en').text)
#
#
# print('Ingrese texto')
# text = input()
#inciar  virtuoso
#virtuoso-t -fd
class TraductorView(TemplateView):
    template_name = 'traductor/index.html'
    def get(self,request):
        form = TraductorForm()
        return render(request, self.template_name ,{'form': form})

    def post(self, request):
        form = TraductorForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['texto']
            idm = form.cleaned_data['idioma']
            form = TraductorForm
            txt=translator.translate(text, dest=idm).text

        args = {'form':form,'txt':txt}
        return render(request, self.template_name, args)
