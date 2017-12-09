

class LojbanNumber:
    loj_to_eng = {
        'no': 0,
        'pa': 1,
        're': 2,
        'ci': 3,
        'vo': 4,
        'mu': 5,
        'xa': 6,
        'ze': 7,
        'bi': 8,
        'so': 9
    }

    eng_to_loj = {v: k for k, v in loj_to_eng.items()}

    def __init__(self, input):
        if type(input) == int:
            self.value = input

        elif type(input) == str:
            integer = 0
            for i in range(0, len(input), 2):
                letters = input[i:i + 2]
                integer *= 10
                integer += self.loj_to_eng[letters]

            self.value = integer



    def toLojban(self):
        lojban = ''
        s = str(self.value)
        for i in s:
            lojban += self.eng_to_loj[int(i)]

        return lojban


    def toEnglish(self):
        return self.value

    def __str__(self):
        return '{} or {}'.format(self.value, self.toLojban())

    def __add__(self, other):
        if type(other) == LojbanNumber:
            return self.value + other.value
        else:
            return self.value + other


if __name__ == "__main__":

    x = LojbanNumber(123)
    y = LojbanNumber('renonore')

    print(x + y)
    print(y.toEnglish())



