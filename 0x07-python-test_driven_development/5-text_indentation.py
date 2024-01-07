#!/usr/bin/python3
def text_indentation(text):
    """ function that prints a text with 2 new
    lines after each of these characters: ., ? and :

    Args:
    text (string): the string text.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for delimeter in "?:.":
        text = (delimeter + "\n\n").join(
                [index.strip(" ") for index in text.split(delimeter)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
