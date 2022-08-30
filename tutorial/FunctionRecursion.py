# wwwwoooorrrlllddd => world

def clean_word(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:  # wwwwoooorrrlllddd
        return clean_word(word[1:])  # wwwoooorrrlllddd
    else:
        return word[0] + clean_word(word[1:])


print(clean_word("sssssshhhhheeeehhhhaaabbb"))
