from pprint import pprint

import pandas as pd
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, FormView
from .forms import UserLoanForm
from django.contrib import messages
from core.settings import BASE_DIR
import os
import pickle
import json
from sklearn.metrics import accuracy_score
import joblib

import numpy as np

model_dir = (os.path.join(BASE_DIR, "ml/models/"))


class IndexView(View):

    def get(self, request):
        context = {'form': UserLoanForm}
        return render(request, 'index.html', context=context)

# class IndexView(FormView):
#     template_name = 'index.html'
#     form_class = UserLoanForm
#     success_url = '/'
#
#     def form_valid(self, form):
#         # perform a action here
#         data = pd.DataFrame({'x': form.cleaned_data}).transpose()
#         data.replace(
#             {'Married': {'No': 0, 'Yes': 1}, 'Gender': {'MALE': 1, 'FEMALE': 0},
#              'Self_Employed': {'No': 0, 'Yes': 1},
#              'Property_Area': {'RURAL': 0, 'SEMI-URBAN': 1, 'URBAN': 2},
#              'Education': {'GRADUATE': 1, 'NOT-GRADUATE': 0}}, inplace=True)
#         x = data.drop(columns=['Firstname', 'Lastname', 'Email', 'Phone'], axis=1)
#         read_model = open(model_dir + "svm_model.pick", "rb")
#         model = pickle.load(read_model)
#         read_model.close()
#         predicted_data = model.predict(x)
#
#         if (predicted_data[0] == 'N'):
#             messages.error(self.request, "you are not eligible for loan")
#         else:
#             messages.success(self.request, "you are eligible for loan")
#         return super().form_valid(form)

def create_response(title, message, type):
    response = {}
    response['title'] = title
    response['message'] = message
    response['type'] = type
    return HttpResponse(
        json.dumps(response, ensure_ascii=False),
        content_type='application/json',
    )

def create_model(form):
    data = pd.DataFrame({'x': form.cleaned_data}).transpose()
    data.replace(
        {'Married': {'No': 0, 'Yes': 1}, 'Gender': {'MALE': 1, 'FEMALE': 0},
         'Self_Employed': {'No': 0, 'Yes': 1},
         'Property_Area': {'RURAL': 0, 'SEMI-URBAN': 1, 'URBAN': 2},
         'Education': {'GRADUATE': 1, 'NOT-GRADUATE': 0}}, inplace=True)
    x = data.drop(columns=['Firstname', 'Lastname', 'Email', 'Phone'], axis=1)
    return x


class SVMView(View):
    form_class = UserLoanForm
    initial = {'key': 'value'}
    template_name = 'form_template.html'

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            x = create_model(form)
        else:
            messages.success(self.request, "Invalid form for loan")
            return redirect('/')
        read_model = open(model_dir + "svm_model.pick", "rb")
        model = pickle.load(read_model)
        read_model.close()
        predicted_data = model.predict(x)
        print(predicted_data)

        if (predicted_data[0] == 'N'):
            messages.error(self.request, "you are not eligible for loan")
            return create_response("Loan Failure", "you are not eligible for loan using SVM", "danger")
        else:
            messages.success(self.request, "you are eligible for loan")
            return create_response("Loan Success", "you are eligible for loan using SVM", "success")


class DeepLearningView(View):
    form_class = UserLoanForm
    initial = {'key': 'value'}

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            data = pd.DataFrame({'x': form.cleaned_data}).transpose()
            x_test = data.drop(columns=['Firstname', 'Lastname', 'Email', 'Phone'], axis=1)
            x_test = pd.get_dummies(x_test)
            print(x_test)
        else:
            messages.success(self.request, "Invalid form for loan")
            return redirect('/')
        md1 = joblib.load(model_dir+'conv.pick')
        # md1 = np.expand_dims(md1, axis=0)
        y_pred = md1.predict(x_test)
        y_pred = (y_pred > 0.52)

        if (y_pred[0]):
            messages.error(self.request, "you are not eligible for loan")
        else:
            messages.success(self.request, "you are eligible for loan")
        pass


class LogisticRegressionView(View):
    form_class = UserLoanForm
    initial = {'key': 'value'}

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            x = create_model(form)
        else:
            messages.success(self.request, "Invalid form for loan")
            return redirect('/')
        save_logistic_model = open(model_dir+"logistic.pick", "rb")
        model = pickle.load(save_logistic_model)
        save_logistic_model.close()
        predicted_data = model.predict(x)
        print(predicted_data)

        if (predicted_data[0] == 0):
            messages.error(self.request, "you are not eligible for loan")
            return create_response("Loan Failure", "you are not eligible for loan using Logistic Regression", "danger")
        else:
            messages.success(self.request, "you are eligible for loan")
            return create_response("Loan Success", "you are eligible for loan using Logistic Regression", "success")


class DecisionTreeView(View):
    form_class = UserLoanForm
    initial = {'key': 'value'}

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            x = create_model(form)
        else:
            messages.success(self.request, "Invalid form for loan")
            return redirect('/')

        save_decision_model = open(model_dir+"decision.pick", "rb")
        model = pickle.load(save_decision_model)
        save_decision_model.close()
        predicted_data = model.predict(x)
        print(predicted_data)

        if (predicted_data[0] == 0):
            messages.error(self.request, "you are not eligible for loan")
            return create_response("Loan Failure", "you are not eligible for loan using Decision Tree", "danger")
        else:
            messages.success(self.request, "you are eligible for loan")
            return create_response("Loan Success", "you are eligible for loan using Decision Tree", "success")


class RandomForestView(View):
    form_class = UserLoanForm
    initial = {'key': 'value'}

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            x = create_model(form)
        else:
            messages.success(self.request, "Invalid form for loan")
            return redirect('/')

        save_random_model = open(model_dir+'random.pick', "rb")
        model = pickle.load(save_random_model)
        save_random_model.close()
        predicted_data = model.predict(x)
        print(predicted_data)

        if (predicted_data[0] == 0):
            messages.error(self.request, "you are not eligible for loan")
            return create_response("Loan Failure", "you are not eligible for loan using Random Forest", "danger")
        else:
            messages.success(self.request, "you are eligible for loan")
            return create_response("Loan Success", "you are eligible for loan using Random Forest", "success")
