def main():
    try:
        with open('books/frankenstein.txt', 'r') as file:
            content = file.read()
            print("--- Begin report of books/frankenstein.txt ---")
            
            words_counted = word_count(content)
            print(words_counted, " words found in the document\n\n")

            char_freq = char_count(content)
            print_character_frequencies(char_freq)

            print("--- End report ---")

    except FileNotFoundError:
        print("The file 'frankenstein.txt' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def word_count(text):
    words = text.split()
    count = 0

    for i in words:
        count += 1
    return (count)

def char_count(text):
    char_frequency = {}
    text = text.lower()

    for char in text:
        if char.isalpha():
            if char in char_frequency:
                char_frequency[char] += 1
            else:
                char_frequency[char] = 1
    
    return (char_frequency)

def print_character_frequencies(char_freq):
    sorted_char_freq = sorted(char_freq.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_char_freq:
        print(f"The '{char}' character was found {count} times")


if __name__ == "__main__":
    main()
