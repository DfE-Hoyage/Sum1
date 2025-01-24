from leap_year import leap_year_check

def test_leap_year_ok():
    assert leap_year_check(2024) ==True

def test_leap_year_wrong():
    assert leap_year_check(2025) == False
