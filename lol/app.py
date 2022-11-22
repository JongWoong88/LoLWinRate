from flask import Flask, jsonify, request, render_template
from models import calWinRate, recommendChamp
import numpy as np
import pickle
app = Flask(__name__,)

@app.route('/lol/winRateModel')
def winRateModel():
    with open("champDict.pickle", "rb") as fr:
        champDict = pickle.load(fr)
    return render_template("winRateModel.html", champDict=champDict)

@app.route('/lol/recommendModel')
def recommendModel():
    with open("champDict.pickle", "rb") as fr:
        champDict = pickle.load(fr)
    return render_template("recommendModel.html", champDict=champDict)

@app.route('/lol/predWinRate', methods=['POST'])
def predWinRate():
    data = {}
    champList = request.json['champList']
    winRate = int(float(calWinRate(champList))*1000)
    data['redWinRate'] = winRate/10
    data['blueWinRate'] = (1000-winRate)/10
    return jsonify(data)

@app.route('/lol/recommendPick', methods=['POST'])
def recommendPick():
    with open("champDict.pickle", "rb") as fr:
        champDict = pickle.load(fr)

    data = {}
    champList = request.json['champList']
    position = request.json['position']
    res = recommendChamp(champList=champList, position=position)
    data['first'] = {"champion": res[0][1],
                   "winRate": int(float(res[0][0])*1000)/10,
                   "name": champDict[res[0][1]]}
    data['second'] = {"champion": res[1][1],
                   "winRate": int(float(res[1][0])*1000)/10,
                   "name": champDict[res[1][1]]}
    data['third'] = {"champion": res[2][1],
                   "winRate": int(float(res[2][0])*1000)/10,
                   "name": champDict[res[2][1]]}
    return jsonify(data)

@app.route('/lol/doc0')
def doc0():
    return render_template("doc0.html")

@app.route('/lol/doc1')
def doc1():
    return render_template("doc1.html")

@app.route('/lol/doc2')
def doc2():
    return render_template("doc2.html")

@app.route('/lol/doc3')
def doc3():
    return render_template("doc3.html")

@app.route('/lol/doc4_1')
def doc4_1():
    return render_template("doc4_1.html")

@app.route('/lol/doc4_2')
def doc4_2():
    return render_template("doc4_2.html")

@app.route('/lol/doc4_3')
def doc4_3():
    return render_template("doc4_3.html")

@app.route('/lol/doc5_1')
def doc5_1():
    return render_template("doc5_1.html")

@app.route('/lol/doc5_2')
def doc5_2():
    return render_template("doc5_2.html")

@app.route('/lol/doc5_3')
def doc5_3():
    return render_template("doc5_3.html")

@app.route('/lol/doc6')
def doc6():
    return render_template("doc6.html")

@app.route('/lol/doc7')
def doc7():
    return render_template("doc7.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)