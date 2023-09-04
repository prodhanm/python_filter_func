import re
from data_dict import names

def match_name(item):
    try:
        pattern = re.compile("M[a-z]+")
        return pattern.match(item)
    except TypeError as err:
        print(f"the variable item must be a string: {err}")

def main():
    try:
        matched_names = list(filter(match_name,names))
        #print(f"names = {matched_names}")
        for name in range(len(matched_names)):
            print(matched_names[name])
    except ValueError as err:
        print(err)

if __name__ == "__main__":
    main()