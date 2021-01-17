from shared_function.function_b import list_to_string


def test_function_b_success():
    assert "1 2" == list_to_string([1, 2], " ")
