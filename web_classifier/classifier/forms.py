from django import forms

class UploadFileForm(forms.Form):
    data = forms.FileField(label = 'Upload do arquivo:')
    knn = forms.BooleanField(label='KNN', required=False)
    svm = forms.BooleanField(label='SVM', required=False)
    tree = forms.BooleanField(label='Decision Tree', required=False)
    