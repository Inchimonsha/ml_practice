class Stats:
    def __init__(self, data: list):
        """
        data - Данные для анализа (тип: list)
        mean - Среднее значение == numpy.mean(x)
        deviation - Дисперсия == numpy.std(x)**2
        standard_deviation - Стандартное отклонение == numpy.std(x)
        standard_error - Стандартная ошибка среднего (se)
        """

        self.data = data
        self.mean = sum(self.data) / len(self.data)
        self.deviation = sum([(i - self.mean) ** 2 for i in self.data]) / len(self.data)
        self.standard_deviation = self.deviation ** 0.5
        self.standard_error = self.standard_deviation / (len(self.data) - 1) ** 0.5

    @property
    def printer(self):
        return f'data: {self.data}\nmean: {self.mean}\ndeviation: {self.deviation}\nstandard_deviation: {self.standard_deviation}\nstandard_error: {self.standard_error}'

    @property
    def z_score(self):
        z_score = [round((i - self.mean) / self.deviation, 2) for i in self.data]
        return z_score

    def confidence_interval(self, y=1.96):
        """ https://en.wikipedia.org/wiki/Standard_deviation#Rules_for_normally_distributed_data
        Confidence interval: 1.959964σ; Proportion within: 95%;         Proportion without: 5%
        Confidence interval: 2σ;        Proportion within: 95.4499736%; Proportion without: 4.5500264%
        Confidence interval: 2.575829σ; Proportion within: 99%;         Proportion without: 1%
        Confidence interval: 3σ;        Proportion within: 99.7300204%; Proportion without: 0.2699796%
        """

        rounding_sd = round(self.standard_deviation)  # 4
        rounding_se = rounding_sd / (len(self.data)) ** (1 / 2)  # 0.5

        return f'{round(self.mean - y * rounding_se, 2)}|------- {self.mean} ------|{round(self.mean + y * rounding_se, 2)}'


x = [102, 91, 99, 100, 103, 98, 99, 101, 106, 88, 103, 97, 103, 101, 101,
     91, 104, 105, 105, 100, 101, 91, 99, 98, 107, 102,
     100, 97, 98, 104, 100, 98, 102, 99, 95, 103, 104, 97, 99, 102, 98, 107,
     101, 93, 98, 101, 93, 91, 107, 102, 96, 93, 100, 105,
     103, 107, 99, 102, 106, 102, 94, 104, 103, 102]

t1 = Stats(x)
print(t1.printer)
print(t1.z_score)
print(t1.confidence_interval(1.96))  # 99.02 |------- 100.0 ------| 100.98