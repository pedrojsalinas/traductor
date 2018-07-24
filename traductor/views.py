from django.shortcuts import render
from django.template import loader
from django.views.generic import TemplateView
from traductor.forms import TraductorForm
from django.http import HttpResponse
#libreria google translator
from googletrans import Translator
#libreria json
import json

translator = Translator()

class TraductorView(TemplateView):
    #nombre de la plantilla html
    template_name = 'traductor/index.html'
    #request obtiene solicitud del formulrio enviado
    def get(self,request):
        #obtiene el metodo get y datos
        form = TraductorForm(request.GET)
        #verifica si el formulario es valido
        if form.is_valid():
            #input texto
            text = form.cleaned_data['texto']
            #input idioma
            idm = form.cleaned_data['idioma']
            #formulario en blanco
            form = TraductorForm
            #llamada a la libreia googletrans con su metodo translate
            #recibe 2 parametros texto e idioma
            txt=translator.translate(text, dest=idm).text
            #creas un arreglo para presentar json
            lista = []
            #agregas objeto al arreglo
            lista.append({"texto":txt,"idioma":idm})
            # print str((HttpResponse(json.dumps(lista), content_type="application/json")))
            #transformas objeto a formato json y se imprime en la consola
            print (str(json.dumps(lista)))
            #objecto con argumentos a presentar en la plantilla
            args = {'form':form,'txt':txt}
            #retornas la plantilla con el texto traducido y args
            return render(request, self.template_name ,args)
        return render(request, self.template_name ,{'form': form})
