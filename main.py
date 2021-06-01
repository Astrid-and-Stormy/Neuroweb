from flask import Flask, render_template, request
from math import e

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route("/learning", methods=['POST', 'GET'])
def learning():
    return render_template('Learning.html', data=request.form, Num_of_ribs=int(request.form['Num_of_ribs']),
                           Num_of_inputs=int(request.form['Num_of_inputs']))


@app.route("/answer", methods=['POST', 'GET'])
def answer():
    prototypes, inputs, outputs, MSE = counter(request.form)
    Num_of_tops = int(request.form['Num_of_tops'])
    return render_template('Answer.html', ans=request.form, prototypes=prototypes,
                           inputs=inputs, outputs=outputs, MSE=MSE, Num_of_tops=Num_of_tops)


def counter(data):
    outputs = {}
    inputs = {}
    for i in range(int(data['Num_of_inputs'])):
        inputs[int(data[f'{i}_index'])] = float(data[f'{i}_input'])
        outputs[int(data[f'{i}_index'])] = float(data[f'{i}_input'])
    prototypes = {}
    for i in range(int(data['Num_of_ribs'])):
        cur = int(data[f'{i}_in'])
        if cur in prototypes.keys():
            prototypes[cur].append([int(data[f'{i}_out']), float(data[f'{i}_rib'])])
        else:
            prototypes[cur] = [[int(data[f'{i}_out']), float(data[f'{i}_rib'])]]
    outputs_tops = set(prototypes.keys())
    for key in prototypes.keys():
        inp = 0
        for connection in prototypes[key]:
            inp += outputs[connection[0]] * connection[1]
            outputs_tops -= {connection[0]}
        inputs[key] = round(inp, 2)
        outputs[key] = round(func(inp, data['Function']), 2)
    MSE = 0
    for tops in outputs_tops:
        if outputs[tops] > 0.5:
            MSE += pow((outputs[tops] - 1), 2)
        else:
            MSE += pow(outputs[tops], 2)
    MSE /= len(outputs_tops)
    return prototypes, inputs, outputs, MSE


def func(a, f):
    if f == 'Lineal':
        return a
    elif f == 'Sigma':
        return 1 / (1 + pow(e, -a))
    return (pow(e, 2 * a) - 1) / (pow(e, 2 * a) + 1)
