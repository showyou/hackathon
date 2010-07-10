import sys
import os

sys.path.insert(
    0,
    os.path.abspath(os.path.dirname(__file__)).rsplit("/",1)[0],
)
import balance
import nose


def test_getDate():
    assert '2010-07-10' == balance.getDate()


if __name__ == '__main__':
    nose.main()
