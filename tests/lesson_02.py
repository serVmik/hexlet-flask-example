import pytest

from course_tests.lesson_02 import function_this_exception


def test_exception():
    with pytest.raises(Exception):
        function_this_exception(0)

