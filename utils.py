import numpy as np
import os
import pickle
import json
import config

class ASD_Detection():
    def __init__(self,A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, age, gender, jaundice, Family_mem_with_ASD):
        self.age = age
        self.gender = gender
        self.A1 = A1
        self.A2 = A2
        self.A3 = A3
        self.A4 = A4
        self.A5 = A5
        self.A6 = A6
        self.A7 = A7
        self.A8 = A8
        self.A9 = A9
        self.A10 = A10
        self.jaundice = jaundice
        self.Family_mem_with_ASD = Family_mem_with_ASD
        self.Qchat_Score = np.sum([A1,A2,A3,A4,A5,A6,A7,A8,A9,A10])

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.model = pickle.load(file) 
        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data = json.load(file) 

    def detect_ASD(self):
        self.load_model()
        arr1 = np.zeros(len(self.json_data["columns"]))
        arr1[0] = self.A1
        arr1[1] = self.A2
        arr1[2] = self.A3
        arr1[3] = self.A4
        arr1[4] = self.A5
        arr1[5] = self.A6
        arr1[6] = self.A7
        arr1[7] = self.A8
        arr1[8] = self.A9
        arr1[9] = self.A10
        arr1[10] = self.age
        arr1[11] = self.gender
        arr1[12] = self.jaundice
        arr1[13] = self.Family_mem_with_ASD
        arr1[14] = self.Qchat_Score
        print("***** ", arr1)
        ASD_result = self.model.predict([arr1])
        return ASD_result








