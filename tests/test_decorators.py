from tests.conftest import test_1, test_2, test_3, test_4


def test_decorators(capsys):
    print(test_1(12))
    captured = capsys.readouterr()
    assert captured.out == "test_1 24\n"
    print(test_2(15, "15"))
    captured = capsys.readouterr()
    assert captured.out == "test_2 error: TypeError. Inputs: (15, '15'), {}\n"
    test_3(15)
    file = open("log_test", "r")
    assert file.read() == "test_3 30"
    test_4(10, "50")
    file = open("error_test", "r")
    assert file.read() == "test_4 error: TypeError. Inputs: (10, '50'), {}"
