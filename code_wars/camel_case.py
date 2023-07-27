def to_camel_case(text):
    words = text.replace("-", "_").split("_")
    camel_case = words[0] + ''.join(word.capitalize() for word in words[1:])

    return camel_case
