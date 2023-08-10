import string
def tokenize_text(text):
    return text.split()

def remove_punctuation(word):
    return word.translate(str.maketrans('', '', string.punctuation))

def count_word_frequency(tokens):
    word_freq = {}
    for token in tokens:
        word = remove_punctuation(token.lower())
        if word:
            word_freq[word] = word_freq.get(word, 0) + 1
    return word_freq

def main():
    with open("C:/Users/Acer/Desktop/FOD/ai.txt","r") as file:
        text = file.read()

    tokens = tokenize_text(text)

    word_freq = count_word_frequency(tokens)

    print("Word Frequency Distribution:")
    for word, frequency in word_freq.items():
        print(f"{word}: {frequency}")

if __name__ == "__main__":
    main()
