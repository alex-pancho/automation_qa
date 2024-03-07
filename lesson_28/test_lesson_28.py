import pytest


@pytest.mark.parametrize("_input, expected",
                         [
                             (1, 2),
                             (2, 3),
                             (3, 4)
                         ]
                         )
def test_increment(_input, expected):
    assert _input + 1 == expected

@pytest.fixture(params=[(1, 2), (2, 3), (3, 4)])
def input_data(request):
    return request.param


def test_increment_second(input_data):
    _input, expected = input_data
    assert _input + 1 == expected


# @pytest.mark.xfail  # if test failed
# @pytest.mark.skipif(env == "windows")  # skip if env is windows
# @pytest.mark.smoke
# def test_smoke():
#     pass
