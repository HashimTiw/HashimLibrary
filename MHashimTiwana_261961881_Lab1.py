#Lab 1

#Q2

def customize_sntnce(sentence):
    words=sentence.split()
    customized_words=[]

    for word in words:
        if word[0].lower() in 'aeiou':
            customized_words.append(word + 'ay')
        else:
            frst_vowel = next((i for i, c in len(word) if c.lower() in 'aeiou'), None)
            customized_words.append(word[frst_vowel:] + word[:first_vowel_index])

    customize_sntnce = ' '.join(customized_words)
    return customize_sntnce
