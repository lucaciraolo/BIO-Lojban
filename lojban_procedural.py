from functools import reduce

def lojban(input):
    dictionary = {'re':2, 'no':0, 'pa': 1, 'ci':3, 'vo':4, 'mu':5, 'xa':6, 'ze':7, 'bi':8, 'so':9}

    s = ''
    for i in range(0, len(input), 2):
        letters = input[i:i + 2]
        s += dictionary[letters]

    return int(s)


print(lojban('sovo') + lojban('rexa'))
