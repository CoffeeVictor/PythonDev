from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from classifier.forms import UploadFileForm
from classifier.models import Dataset
from classifier.ML import trainCSV

def index(request):
    form = UploadFileForm()
    context = {'form': form}
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Dataset(data_file = request.FILES['data'])
            newdoc.save()
            search_id = newdoc.id
            x = Dataset.objects.get(id = search_id)
            file_path = trainCSV(str(x.data_file.open()), form['knn'].value(), form['svm'].value(), form['tree'].value())
            context['image_path'] = file_path
            context['file'] = request.FILES['data']


    return render(request, 'index.html', context)
