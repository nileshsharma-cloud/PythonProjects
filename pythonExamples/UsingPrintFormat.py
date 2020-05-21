import sys

def test_pass(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "this is at line number {0} ok.",format(linenum)
    else:
        msg = "this is at line number {0} failed.", format(linenum)
        print(msg)
        
def test_suite():
    test_pass(abs(-17)==17)
    
test_suite()