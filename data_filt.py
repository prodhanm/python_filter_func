import re
from data_dict import names

def match_name():
    for name in names:
        pattern = re.compile("M[a-z]+")
        data = pattern.match(name)
        if not None:
            print(data.groups())

match_name()