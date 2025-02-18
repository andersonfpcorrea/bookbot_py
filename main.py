from operator import contains


def count_chars(words: str):
    d = {}
    for w in words:
        wl = w.lower()
        if wl in d:
            d[wl] += 1
        else:
            d[wl] = 1
    return d
    

with open("./books/frankenstein.txt") as f:
    file_contents = f.read()
    words = file_contents.split()
    report = count_chars(file_contents)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{len(words)} words found in the document")
    print("\n")
    not_allowed = {" ", ".", "#"}
    for k in report:
        if contains(not_allowed, k): 
            continue
        print(f"The '{k}' character was found {report[k]} times")