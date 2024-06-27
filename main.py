

def word_count(source):
    words = source.split()
    return len(words)
    
def char_count(source):
    x = {}
    lowered_string = source.lower()
    for i in lowered_string:
        if i.isalpha():
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
    return x

def chars_sorted(x):
    for i in sorted(x.keys()):
        y = x[i]
        print(f"{i} appeared {y} times in this book")


def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
    # print(file_contents)
    # return file_contents

    print("--- Begin report of Frankenstein ---")
    
    a = word_count(file_contents)

    print(f"{a} words found in the document")
    
    chars_sorted(char_count(file_contents))

main()