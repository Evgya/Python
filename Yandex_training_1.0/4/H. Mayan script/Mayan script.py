def count_possible_words(word, sen):
    w_dict = dict()
    for symbol in word:
        w_dict[symbol] = w_dict.setdefault(symbol, 0) + 1

    cur_dict = dict()
    for symbol in sen[0: len(word)]:
        if symbol in w_dict:
            cur_dict[symbol] = cur_dict.setdefault(symbol, 0) + 1

    bool_dict = {
        x: w_dict[x] == cur_dict.setdefault(x, 0) for x in w_dict.keys()
        }

    true_count = sum(bool_dict.values())
    counter = 0
    if true_count == len(bool_dict):
        counter = 1

    for left_border in range(len(sen) - len(word)):
        right_border = left_border + len(word)

        if sen[left_border] in w_dict:
            cur_dict[sen[left_border]] -= 1
            if bool_dict[sen[left_border]]:
                bool_dict[sen[left_border]] = False
                true_count -= 1
            elif cur_dict[sen[left_border]] == w_dict[sen[left_border]]:
                bool_dict[sen[left_border]] = True
                true_count += 1

        if sen[right_border] in w_dict:
            cur_dict[sen[right_border]] += 1
            if bool_dict[sen[right_border]]:
                bool_dict[sen[right_border]] = False
                true_count -= 1
            elif cur_dict[sen[right_border]] == w_dict[sen[right_border]]:
                bool_dict[sen[right_border]] = True
                true_count += 1
        if true_count == len(bool_dict):
            counter += 1

    return counter

nG, nS = map(int, input().split())
G = input()
S = input()
print(count_possible_words(G, S))
