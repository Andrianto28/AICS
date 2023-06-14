from django.shortcuts import render
from django.http import HttpResponse

from django.http import JsonResponse
#from .models import Predictor
#from .serializers import PredictorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import os
from flask import Flask, request, jsonify
import pytesseract
import re
import cv2
import numpy as np
import json

from django.conf import settings

from locationMovement3.apiDeploy.libraries import *

# views for Ai Location movement.
@api_view(['POST'])
def predictloc(request):
    try:
        content_type = request.headers.get("Content-Type")
        if content_type == "application/json":
            # Get json data
            #json_data = request.get_json()
            json_data = request.data

            # Convert json to dataframe
            df_input = pd.DataFrame.from_dict(json_data, orient="index").T

            # Convert specific columns to numeric data type
            numeric_columns = [
                "domicile_lat",
                "domicile_lon",
                "now_lat",
                "now_lon",
                "last_1_week_lat",
                "last_1_week_lon",
                "last_2_week_lat",
                "last_2_week_lon",
                "last_3_week_lat",
                "last_3_week_lon",
                "last_4_week_lat",
                "last_4_week_lon",
            ]
            df_input[numeric_columns] = df_input[numeric_columns].apply(pd.to_numeric)

            # Preprocess Data
            preprocessed_data = data_preprocessing(df_input)
            print(preprocessed_data)

            reshaped_data = np.reshape(
                preprocessed_data, (preprocessed_data.shape[0], -1)
            )

            result = model.predict(reshaped_data)[0]
            # return JsonResponse(dict, status=status.HTTP_200_OK)
            return JsonResponse(
                {
                    "input": json_data,
                    "status": True,
                    "message": "success",
                    "result": result
                }, 
                status=status.HTTP_200_OK
            )
    except Exception as e:
        return JsonResponse(
            {"status": False, "message": "Data is not valid", "error": str(e)}
        )
        #return jsonify({"status": False, "message": "Data is not valid", "error": str(e)})