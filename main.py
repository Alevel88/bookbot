def count(string):
    count = 0
    words = string.split()
    number_of_rows = len(words)
    for i in range(0, number_of_rows):
        count += 1
    return count


def count_char(string):
    alphabet_string = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    count_lett_dict = {}
    words = list(string)
    for i in range(len(words)):
        letter = words[i]
        letter =  letter.lower()
        if letter.isalpha(): 
            if letter in count_lett_dict:
                count_lett_dict[letter] +=1
            else:
                count_lett_dict[letter] =1    

    return count_lett_dict

def report(letters):
    print('--- Begin report of books/frankenstein.txt ---')
    sorted_words=sorted(letters.items(),key=lambda item: int(item[1]))
    print(sorted_words)
    print('--- End report ---')

def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
#    print(file_contents)
    words = count(file_contents)
    print(words)
    letters = count_char(file_contents)
    report(letters)



main()