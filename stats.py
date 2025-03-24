def get_num_words(content):
    num_words = len(content.split())
    return f"Found {num_words} total words"

def get_num_chars(content):
    words = content.split()
    char_num = {}
    for word in words:
        word = str.lower(word)
        for char in word:
            if char in char_num:
                char_num[char] += 1
            else:
                char_num[char] = 1
    return char_num