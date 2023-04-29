def count_strings_by_character(list, character) -> int:
    """Return the count of strings starting with the given character"""
    count = 0
    for string in list:
        if string.startswith(character):
            count += 1
    return count
