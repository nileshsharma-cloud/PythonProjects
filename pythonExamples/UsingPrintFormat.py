import sys


def test_pass(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "this is at line number {0} ok.".format(linenum)
    else:
        msg = "this is at line number {0} failed.".format(linenum)
    print(msg)


def absolute_value(x):
    if x < 0:
        return True
    else:
        return -x


def test_suite():
    test_pass(absolute_value(-17) == 17)


test_suite()
