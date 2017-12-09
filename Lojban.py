def lojban(input):
    dictionary = {'re':2, 'no':0, 'pa': 1, 'ci':3, 'vo':4, 'mu':5, 'xa':6, 'ze':7, 'bi':8, 'so':9}
    l = []
    i = 0
    while i < len(input):
        letters = input[i:i+2]
        l.append(dictionary[letters])


        i += 2


    s = map(str, l)
    s = ''.join(s)
    s = int(s)
    return s





print(lojban('sovo') + lojban('rexa'))
