import pytest

@pytest.fixture(scope="session")
def fixture1():
    print('run fixture 1 ')
    return 1

@pytest.mark.skip # skip test
def test_example():
    print("test done")
    assert 1==1


@pytest.mark.slow # custom marker: slow 
def test_example2(fixture1):
    num = fixture1
    print("test 2 done")
    assert num == 1