from math import e
num_of_tops = int(input('Введите количество вершин: '))
func = int(input('Введите тип функции (1 - линейная, 2 - сигмовидная, 3 - гиперболический тангенс) '))
inputs = {}  # Список входных значений
prototypes = {}  #Двумерный Список прообразов
weights = {}  #Cловарь списков весов дуг
outputs = {}
neurons = [] #Веришны, не являющиеся входными

for i in range(num_of_tops):
    prototypes[i] = list(map(int, input('Введите проообразы вершины ' + str(i) + ' через пробел: ').split()))
    if len(prototypes[i]) == 0:
        inputs[i] = float(input('Введите входной сигнал веришны ' + str(i) + ': '))
    else:
        neurons.append(i)
        weights[i] = list(map(float, input('Введите веса дуг, соединяющих вершину ' + str(i) + ' с веришнами ' + ' '.join(map(str, prototypes[i])) + ': ').split()))

def f(a, func):
    if func == 1:
        return a
    elif func == 2:
        return 1/(1+pow(e, -a))
    return((pow(e, 2*a)-1)/(pow(e, 2*a)+1))

print('x; prototypes x; input(x); output(x)')
for i in inputs.keys():
    print(i, '-', inputs[i], inputs[i])
    outputs[i] = inputs[i]
for i in neurons:
    cur_input = 0
    for j in range(len(prototypes[i])):
        cur_input += outputs[prototypes[i][j]]*weights[i][j]
    outputs[i] = f(cur_input, func)
    print(i, ' '.join(map(str, prototypes[i])), round(cur_input, 2), round(outputs[i], 2), sep = "; ")