# put your python code here
def calculate_words(_sentence):
    words_frequency = dict()
    for word in _sentence:
        if word.lower() in words_frequency:
            words_frequency[word.lower()] += 1
        else:
            words_frequency[word.lower()] = 1
    return words_frequency


sentence = input().split()
for key, value in calculate_words(sentence).items():
    print(key, value)