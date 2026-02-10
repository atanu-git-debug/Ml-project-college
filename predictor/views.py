from django.shortcuts import render
import os
import pickle
import numpy as np
from django.conf import settings
from .forms import PredictionForm
# Create your views here.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(os.path.join(BASE_DIR,'model.pkl'),'rb'))
scaler = pickle.load(open(os.path.join(BASE_DIR,'scaler.pkl'),'rb'))

def predict_view(request):
    result = None
    probability = None

    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            salary = form.cleaned_data['salary']

            data = np.array([[age,salary]])
            data = scaler.transform(data)

            pred = model.predict(data)[0]
            
            prob = float(model.predict_proba(data)[0][1])

            probability = round(prob * 100 ,2)
            if pred == 1:
                result = "Customer Will Purches"
            else :
                result = "Customer will not Purches"
            
    else:
        form = PredictionForm()
    context = {
        'form' : form,
        'result' : result,
        'probability' : probability
    }
    return render(request,'predict.html',context)