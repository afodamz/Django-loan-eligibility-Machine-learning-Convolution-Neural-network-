
from django.contrib import admin
from django.urls import path

from app.views import IndexView, SVMView, DeepLearningView, LogisticRegressionView, DecisionTreeView, RandomForestView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('svm', SVMView.as_view(), name='svm'),
    path('deep', DeepLearningView.as_view(), name='deep'),
    path('logistic', LogisticRegressionView.as_view(), name='logistic'),
    path('decision', DecisionTreeView.as_view(), name='decision'),
    path('random', RandomForestView.as_view(), name='random'),
]
