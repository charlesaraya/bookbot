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

def sort_num_chars(char_num):
    char_count = [(key, char_num[key]) for key in char_num]
    char_count.sort(key=lambda x: x[1], reverse=True)
    return char_count