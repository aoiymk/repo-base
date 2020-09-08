import random
import string

#pd.set_option('display.float_format', lambda x: '%.5f' % x)

def random_string(n=6):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(n))

def encript_string(data, columns):
    for c in columns:
        ann = dict([(f, random_string()) for f in data[c].unique()])
        data[c] = data[c].apply(lambda x: ann[x])
    return data

def encript_int(data, columns):
    factor = random.random()
    for c in columns:
        data[c] = data[c].apply(lambda x: int(x * factor))
    return data

def encript_double(data, columns):
    factor = random.random()
    for c in columns:
        data[c] = data[c].apply(lambda x: x * factor)
    return data