
def resolve_extension(filename):
    extension = ''
    for i in range(len(filename)):
        if filename[-i] == '.':
            for j in range(i):
                extension += filename[-j - 1]
            break
    extension = extension[::-1]
    return extension


def remove_from_string(_string, part_to_remove):
    _string = _string.split(part_to_remove)
    new_string = ""
    for i in _string:
        new_string += i
    return new_string


def process_messages(dict):
    _string = ""
    for key in dict:
        _string += f"\n{key}: {dict[key]}"
    return _string


