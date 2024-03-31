from django import template

register = template.Library()


@register.filter
def censor(value):
    if not isinstance(value, str):
        raise ValueError("Censor filter can only be applied to strings.")

    forbidden_words = ['редиска', 'брань1', 'брань2','брань3']

    words = value.split()

    for i, word in enumerate(words):
        for forbidden_word in forbidden_words:
            if word.lower().startswith(forbidden_word.lower()) and word[0].isupper() == forbidden_word[0].isupper():
                censored_word = word[0] + '*' * (len(word) - 1)
                words[i] = censored_word

    return ' '.join(words)

    return result

