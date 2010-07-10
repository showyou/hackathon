import nose
import hackathon


def testAdd():
    assert 3 == hackathon.add(1,2)


def testSub():
    assert 1 == hackathon.sub(2,1)


def testGreeting():
    assert 'Hello, world!' == hackathon.greeting('Hello, world!')


if __name__ == '__main__':
    nose.main()
