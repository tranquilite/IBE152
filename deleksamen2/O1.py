

def question_1(text: str, size: int) -> str:
    text = text.split()
    for word in text:
        word = word.strip().strip('.(),')

        if len(word) == size:
            return word
    
    return ''


if __name__ == '__main__':
    text = """The Python String split() method splits all words in a string separated by a specified separator.
    This separator is a delimiter string, and can be a comma, full stop, space character or any other character used to separare strings.
    Usually, if multiple separators are grouped together, the method treats it as an empty string.
    But if the separator is not specified or is None, and the string consists for consecutive whitespaces, they are regarded as a single separator, and the result will contain no empty strings at the start or end if the string has leading or trailing whitespace.
    Consequently, splitting an empty string or a string consisting of just whitespace with a None separator results in an empty string."""

    print(
        f'>> {question_1(text, 7)}'
        )
