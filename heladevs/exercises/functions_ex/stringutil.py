def count_strings_by_character(strings, character) -> int:
    """Return the count of strings starting with the given character"""
    count = 0
    cap_char = character.capitalize()
    for string in strings:
        cap_string = string.capitalize()
        if cap_string.startswith(cap_char):
            count += 1
    return count

