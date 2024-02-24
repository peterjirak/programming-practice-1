from append_and_delete import append_and_delete

def test_append_and_delete():
    assert append_and_delete(
        'hackerhappy',
        'hackerrank',
        9
    ) == 'Yes'
    assert append_and_delete(
        'aba',
        'aba',
        7
    ) == 'Yes'
    assert append_and_delete(
        'aaaaaaaaaa',
        'aaaaa',
        7
    ) == 'Yes'
    assert append_and_delete(
        'zzzzz',
        'zzzzzzz',
        4
    ) == 'Yes'
    assert append_and_delete(
        'qwerasdf',
        'qwerbsdf',
        6
    ) == 'No'
    assert append_and_delete(
        'y',
        'yu',
        2
    ) == 'No'
    assert append_and_delete(
        'qwerty',
        'zxcvbn',
        100
    ) == 'Yes'
    assert append_and_delete(
        'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
        'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
        20
    ) == 'Yes'
    assert append_and_delete(
        'asdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
        'bsdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcvasdfqwertyuighjkzxcv',
        100
    ) == 'No'
    assert append_and_delete(
        'abcdef',
        'fedcba',
        15
    ) == 'Yes'
    assert append_and_delete(
        'abcd',
        'abcdert',
        10
    ) == 'No'
    assert append_and_delete(
        'uoiauwrebgiwrhgiuawheirhwebvjforidkslweufgrhvjqasw',
        'vgftrheydkoslwezxcvdsqjkfhrydjwvogfheksockelsnbkeq',
        100
    ) == 'Yes'
    assert append_and_delete(
        'aaa',
        'a',
        5
    ) == 'Yes'
    assert append_and_delete(
        'ashley',
        'ash',
        2
    ) == 'No'
