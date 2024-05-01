from flask import Flask,request,jsonify, render_template
import config
from utils import ASD_Detection
import numpy as np

app = Flask(__name__)
@app.route("/")
def get_home():
    return render_template('homepage.html')

@app.route("/predict",methods= ["POST","GET"])
def get_ASD_Detection():
    if request.method == "POST":
        data = request.form
        A1 = request.form.getlist("A1")
        A2 = request.form.getlist("A2")
        A3 = request.form.getlist("A3")
        A4 = request.form.getlist("A4")
        A5 = request.form.getlist("A5")
        A6 = request.form.getlist("A6")
        A7 = request.form.getlist("A7")
        A8 = request.form.getlist("A8")
        A9 = request.form.getlist("A9")
        A10 = request.form.getlist("A10")
        age = int(request.form["age"])
        gender = request.form.getlist("gender")
        jaundice = request.form.getlist("jaundice")
        Family_mem_with_ASD = request.form.getlist("autism")

        if (age >17):
            asd_obj = ASD_Detection(int(A1[1]), int(A2[1]), int(A3[1]), int(A4[1]), int(A5[1]), int(A6[1]), int(A7[1]),
                                     int(A8[1]), int(A9[1]), int(A10[1]), age, int(gender[1]), int(jaundice[1]), int(Family_mem_with_ASD[1]))
        else:
            asd_obj = ASD_Detection(int(A1[0]), int(A2[0]), int(A3[0]), int(A4[0]), int(A5[0]), int(A6[0]), int(A7[0]),
                                     int(A8[0]), int(A9[0]), int(A10[0]), age, int(gender[0]), int(jaundice[0]), int(Family_mem_with_ASD[0]))
        
        result = asd_obj.detect_ASD()
        print("result :",result)
        if result == 1:
            msg1 = "You might be suffering from ASD. Please consult doctor for further diagonsis. "
        else:
            msg1 = "Your ASD result is negative. "    
    return jsonify({"result": msg1})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER,debug=False)




