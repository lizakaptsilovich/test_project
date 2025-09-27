import pytest
from classes.tests_pytest import avg_len, avg_len2

def test_sr_len():
    s=[1,2,3,4,5]
    res=avg_len(s)
    assert res>0

def test_sr_len1():
    s=[1,2,3,4,5]
    res=avg_len(s)
    assert res<0