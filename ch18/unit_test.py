import sys
import time

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def timer(func):
    t0=time.clock()
    func
    t1=time.clock()
    print("That took {} seconds to complete!".format(t1-t0))

