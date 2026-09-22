"""
Tinker 1B, Part 1: write an assert-based pytest test for session_rating()
BEFORE you touch anything else. One test is started for you -- add at least
one more.
"""

from scoring import session_rating


def test_session_rating_boundary_90_is_great():
    assert session_rating(90) == "Great"


# TODO: add at least one more test, e.g. a boundary case for "Skip" (a score
# of 59) or the exact boundary for "Good" (a score of 80).


def test_session_rating_boundary_80_is_good():
    # 80 is the exact lower edge of "Good"; catches off-by-one (> vs >=) bugs.
    assert session_rating(80) == "Good"