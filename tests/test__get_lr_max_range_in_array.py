from tasks_templates.arrays.get_lr_max_range_in_array import get_max_range, get_min_range


def test__default_settings():
    assert get_max_range([1, 2, 5, 5, 7, 3, 10]) == (
        [0, 0, 0, 3, 0, 5, 0],
        [0, 1, 3, 3, 5, 5, 6]
    )


def test__border_values():
    assert get_max_range([5, 5, 5, 7, 7, 10, 11, 11]) == (
        [0, 1, 2, 0, 4, 0, 0, 7],
        [2, 2, 2, 4, 4, 5, 7, 7]
    )


def test__border_values_2():
    assert get_max_range([8, 8, 8, 7, 7, 12, 11, 11]) == (
        [0, 1, 2, 3, 4, 0, 6, 7],
        [4, 4, 4, 4, 4, 7, 7, 7]
    )


def test__flag_ff():
    assert get_max_range([8, 8, 8, 7, 7, 12, 12, 11, 11], borders=(False, False)) == (
        [0, 1, 2, 3, 4, 0, 6, 7, 8],
        [0, 1, 4, 3, 4, 5, 8, 7, 8]
    )


def test__flag_tf():
    assert get_max_range([8, 8, 8, 7, 7, 12, 12, 11, 11], borders=(True, False)) == (
        [0, 0, 0, 3, 3, 0, 0, 7, 7],
        [0, 1, 4, 3, 4, 5, 8, 7, 8]
    )


def test__flag_tt():
    assert get_max_range([8, 8, 8, 7, 7, 12, 12, 11, 11], borders=(True, True)) == (
        [0, 0, 0, 3, 3, 0, 0, 7, 7],
        [4, 4, 4, 4, 4, 8, 8, 8, 8]
    )


def test__get_min_range():
    assert get_min_range([8, 8, 8, 7, 7, 12, 12, 11, 11]) == (
        [0, 1, 2, 0, 4, 5, 6, 5, 8],
        [2, 2, 2, 8, 8, 6, 6, 8, 8]
    )


def test__get_min_range_tt():
    assert get_min_range([8, 8, 8, 7, 7, 12, 12, 11, 11], borders=(True, True)) == (
        [0, 0, 0, 0, 0, 5, 5, 5, 5],
        [2, 2, 2, 8, 8, 6, 6, 8, 8]
    )

