from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView

from django.http import HttpResponseRedirect
from django.urls import reverse

import sklearn


def homePost(request):
    # Use request object to extract choice.

    size, weight, sweetness, softness, harvestTime, ripeness, acidity = 3, 3, 3, 3, 3, 3, 3

    try:
        # Extract value from request object by control name.
        sizeStr = request.POST['size']
        weightStr = request.POST['weight']
        sweetnessStr = request.POST['sweetness']
        softnessStr = request.POST['softness']
        harvestTimeStr = request.POST['harvestTime']
        ripenessStr = request.POST['ripeness']
        acidityStr = request.POST['acidity']

        # Convert string to integer.
        size = int(sizeStr)
        weight = int(weightStr)
        sweetness = int(sweetnessStr)
        softness = int(softnessStr)
        harvestTime = int(harvestTimeStr)
        ripeness = int(ripenessStr)
        acidity = int(acidityStr)

    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The data submitted is invalid. Please try again.',
            'mynumbers': [1, 2, 3, 4, 5, 6]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', kwargs={'size': size,
                                                                'weight': weight,
                                                                'sweetness': sweetness,
                                                                'softness': softness,
                                                                'harvestTime': harvestTime,
                                                                'ripeness': ripeness,
                                                                'acidity': acidity}, ))


import pickle
import pandas as pd

def results(request, size, weight, sweetness, softness, harvestTime, ripeness, acidity):
    sklearn_version = sklearn.__version__

    # load saved model
    with open('helloworld/banana_model2.pkl', 'rb') as f:
        loadedModel = pickle.load(f)

    # Columns: Size,Weight,Sweetness,Softness,HarvestTime,Ripeness,Acidity
    # Create a single prediction.
    singleSampleDf = pd.DataFrame(columns=['Size', 'Weight', 'Sweetness', 'Softness', 'HarvestTime', 'Ripeness', 'Acidity'])

    choice_to_model = {1: -5, 2: -2.5, 3: 0, 4: 2.5, 5: 5}
    model_to_word = {-5: 'Very Low', -2.5: 'Low', 0: 'Average', 2.5: 'High', 5: 'Very High'}

    size = choice_to_model[size]
    weight = choice_to_model[weight]
    sweetness = choice_to_model[sweetness]
    softness = choice_to_model[softness]
    harvestTime = choice_to_model[harvestTime]
    ripeness = choice_to_model[ripeness]
    acidity = choice_to_model[acidity]

    singleSampleDf = singleSampleDf.append({'Size': size, 'Weight': weight, 'Sweetness': sweetness, 'Softness': softness,
                                             'HarvestTime': harvestTime, 'Ripeness': ripeness, 'Acidity': acidity},
                                            ignore_index=True)

    # Load the scaler
    with open('helloworld/banana_scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)

    # Scale the test data
    singleSampleDf = scaler.transform(singleSampleDf)

    singlePrediction = loadedModel.predict(singleSampleDf)

    print("Single prediction: " + str(singlePrediction))


    return render(request, 'results.html', {
        'size': model_to_word[size],
        'weight': model_to_word[weight],
        'sweetness': model_to_word[sweetness],
        'softness': model_to_word[softness],
        'harvestTime': model_to_word[harvestTime],
        'ripeness': model_to_word[ripeness],
        'acidity': model_to_word[acidity],
        'prediction': singlePrediction})



def homePageView(request):
    # return request object and specify page.
    return render(request, 'home.html', {
        'mynumbers': [1, 2, 3, 4, 5, 6],
        'firstName': 'Juan',
        'lastName': 'Escalada'
    })


def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')


def juanPageView(request):
    return render(request, 'juan.html')
