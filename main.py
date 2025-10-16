from stats import *

def main():
    text = get_book_text("books/Frankenstein.txt")
    num = get_word_count(text)
    count = get_char_count(text)
    char_list = []

    for i in count:
        char_list.append({"char": i, "num_times": count[i]})
    
    def sort_on(items):
        return items["char"]
    
    char_list.sort(key = sort_on)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
    for a in char_list:
        print( str(a["char"])+ " : " + str(a["num_times"]))

main()