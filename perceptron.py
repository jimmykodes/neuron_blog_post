import random


class Neuron:
    def __init__(self, number_of_inputs, weights=None, training_rate=0.1):
        self.number_of_inputs = number_of_inputs
        self.weights = weights if weights is not None else self._random_weights()
        self.training_rate = training_rate

    def _random_weights(self):
        return [random.normalvariate(0, .5) for _ in range(self.number_of_inputs)]

    def _weighted_sum(self, inputs):
        return sum([inputs[i] * self.weights[i] for i in range(self.number_of_inputs)])

    def _activate(self, w_sum):
        return -1 if w_sum < 0 else 1

    def _adjust_weights(self, inputs, error):
        for i in range(self.number_of_inputs):
            self.weights[i] += inputs[i] * error * self.training_rate

    def predict(self, inputs):
        w_sum = self._weighted_sum(inputs)
        return self._activate(w_sum)

    def train(self, inputs, label):
        output = self.predict(inputs)
        error = label - output
        self._adjust_weights(inputs, error)

    def test(self, x_test, y_test):
        error = 0
        for i, inputs in enumerate(x_test):
            if self.predict(inputs) != y_test[i]:
                error += 1
        return error / len(x_test)

    def run(self, x, y):
        half = len(x) // 2
        x_train = x[:half]
        x_test = x[half:]
        y_train = y[:half]
        y_test = y[half:]
        error_rates = [self.test(x_test, y_test)]
        for i, inputs in enumerate(x_train):
            self.train(inputs, y_train[i])
            error_rates.append(self.test(x_test, y_test))
        return error_rates
