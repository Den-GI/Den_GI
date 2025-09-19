class Distance:
    def __init__(self, value, unit='m'):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"{self.value} {self.unit}"

    def _to_meters(self):
        if self.unit == 'cm':
            return self.value * 0.01
        elif self.unit == 'm':
            return self.value
        elif self.unit == 'km':
            return self.value * 1000
        else:
            return self.value

    def __add__(self, other):
        total_meters = self._to_meters() + other._to_meters()
        return Distance(total_meters, 'm')

    def __sub__(self, other):
        result_meters = self._to_meters() - other._to_meters()
        if result_meters < 0:
            raise ValueError("Результат не может быть отрицательным")
        return Distance(result_meters, 'm')

