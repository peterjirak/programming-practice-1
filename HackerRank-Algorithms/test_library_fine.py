from library_fine import library_fine

def test_library_fine():
    assert library_fine(
        6, 6, 2015,
        9, 6, 2016
    ) == 0

    assert library_fine(
        9, 6, 2015,
        6, 6, 2015
    ) == 45

    assert library_fine(
        30, 5, 2015,
        2, 5, 2015
    ) == 420

    assert library_fine(
        2, 5, 2015,
        30, 5, 2015
    ) == 0

    assert library_fine(
        2, 7, 1014,
        1, 1, 1014
    ) == 3000

    assert library_fine(
        2, 7, 2015,
        1, 2, 2014
    ) == 10000

    assert library_fine(
        2, 6, 2014,
        5, 7, 2014
    ) == 0

    assert library_fine(
        2, 6, 2014,
        7, 6, 2014
    ) == 0

    assert library_fine(
        1, 1, 2000,
        1, 1, 2000
    ) == 0

    assert library_fine(
        28, 2, 2015,
        15, 4, 2015
    ) == 0

    assert library_fine(
        1, 1, 2001,
        1, 1, 2000
    ) == 10000

    assert library_fine(
        5, 5, 2014,
        23, 2, 2014
    ) == 1500

    assert library_fine(
        31, 5, 2014,
        1, 5, 2014
    ) == 450

    assert library_fine(
        1, 1, 2015,
        31, 12, 2014
    ) == 10000

    assert library_fine(
        31, 8, 2004,
        20, 1, 2004
    ) == 3500

    assert library_fine(
        15, 7, 2014,
        1, 7, 2015
    ) == 0
