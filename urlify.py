def urlify(text: list[str]) -> int:
    spacebars_found = 0
    original_size = 0

    for char in text:
        if char == '':
            break
        if char == ' ':
            spacebars_found += 1
        original_size += 1

    del text[:original_size-1:-1]
    new_size = original_size - 1 + (2 * spacebars_found)
    text += [''] * (2 * spacebars_found)

    fast_index = original_size - 1
    slow_index = new_size

    while fast_index >= 0:
        if text[fast_index] == ' ':
            text[slow_index] = '0'
            text[slow_index-1] = '2'
            text[slow_index-2] = '%'
            slow_index -= 3
        else:
            text[slow_index] = text[fast_index]
            slow_index -= 1

        fast_index -= 1
    return new_size + 1


text = list('my url') + [''] * 21
new_len = urlify(text)

assert new_len == 8
assert text[:new_len] == list('my%20url')

text = list('')
new_len = urlify(text)

assert new_len == 0
assert text[:new_len] == list('')

text = list(' my url ')
new_len = urlify(text)

assert new_len == 14
assert text[:new_len] == list('%20my%20url%20')

text = list(' my   url ')
new_len = urlify(text)

assert new_len == 20
assert text[:new_len] == list('%20my%20%20%20url%20')

text = list(' my url with multiple spaces and words ')
new_len = urlify(text)

assert new_len == 55
assert text[:new_len] == list('%20my%20url%20with%20multiple%20spaces%20and%20words%20')

text = list(' ')
new_len = urlify(text)

assert new_len == 3
assert text[:new_len] == list('%20')

text = list('myurl')
new_len = urlify(text)

assert new_len == 5
assert text[:new_len] == list('myurl')

text = list('  ')
new_len = urlify(text)

assert new_len == 6
assert text[:new_len] == list('%20%20')