import re
from data_dict import names

def match_name(item):
    pattern = re.compile("M[a-z]+")
    return pattern.match(item)

def main():
    matched_names = list(filter(match_name,names))
    #print(f"names = {matched_names}")
    for name in range(len(matched_names)):
        print(matched_names[name])

if __name__ == "__main__":
    main()