from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Approval
from .serializers import ApprovalSerializer
from rest_framework import status
from joblib import load
import numpy as np
from django.http import JsonResponse
from keras._tf_keras.keras.models import load_model

# Create your views here.

class ApprovalView(APIView):
    def get(self, request):
        approvals = Approval.objects.all()
        serializer = ApprovalSerializer(approvals, many=True)
        return Response(serializer.data)

class AddApprovals(APIView):
    def post(self, request):
        try:
            mdl = load_model('loan_model.keras')
            data = request.data
            unit = np.array(list(data.values()))
            unit = unit.reshape(1,-1)
            scalers = load('scaler.pkl')
            X = scalers.transform(unit)
            y_pred = mdl.predict(X)
            y_pred = (y_pred>0.58)            
            response = y_pred
            return Response({"status": bool(response)})
        except ValueError as e:
            return Response(e.args[0], status=status.HTTP_400_BAD_REQUEST)