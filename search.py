file = open("words.txt", encoding='utf-8', mode='r')
arr = file.read().split('\n')

users_input = input('Введите слово: ')

def recursive_search(search_for, vocab, next_vocab):
    if len(search_for) > 0:
        for word in vocab:
            for letter in word:
                if letter == search_for[0]:
                    next_vocab.append(word)
                    break;
        recursive_search(search_for[1:], next_vocab, [])
    else:
        print(vocab)
        return


recursive_search(users_input, arr, [])