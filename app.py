import json

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from perceptron import Neuron


def read_data():
    with open('data.json') as f:
        return json.load(f)


def main():
    sns.set(rc={'figure.figsize': (8, 4)})
    sns.set_style('darkgrid', {'figure.facecolor': '#dddddd', 'axes.facecolor': '#dddddd'})
    n = Neuron(number_of_inputs=2, training_rate=.1)
    data = read_data()
    X = data['X']
    y = data['y']

    error = n.run(X, y)

    df = pd.DataFrame(data=enumerate(error), columns=['iteration', 'error'])
    plt.subplot(1, 2, 1)
    sns.lineplot(x='iteration', y='error', data=df)

    plot_data = []
    for i, point in enumerate(X):
        prediction = n.predict(point)
        label = y[i]
        if prediction == label:
            plot_data.append([*point, label])
        else:
            plot_data.append([*point, 'error'])

    df2 = pd.DataFrame(data=plot_data, columns=['x', 'y', 'label'])
    plt.subplot(1, 2, 2)
    sns.scatterplot(x='x', y='y', data=df2, hue='label', legend=False, palette={-1: 'blue', 1: 'green', 'error': 'red'})

    plt.show()


if __name__ == '__main__':
    main()
