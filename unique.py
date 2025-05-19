if (0.1+0.2 == 0.3):
    print ('True')
else:
    print ('False')

'''
The answer is false due to floating-point precision errors in binary representation.

Q.} Why it happens:

->  Computers represent floating-point numbers (like 0.1, 0.2, and 0.3) in binary using a format called IEEE 754.
    Numbers like 0.1 and 0.2 cannot be exactly represented in binary.
    So, 0.1 + 0.2 results in a number very close to 0.3, but not exactly 0.3.

Q.} How to fix it:

->  Use the `math.isclose()` function to compare floating-point numbers with a tolerance.
    Example:
        import math
        if math.isclose(0.1 + 0.2, 0.3):
            print('True')
        else:
            print('False')
'''

import math
if math.isclose(0.1 + 0.2, 0.3):
    print('True')
else:
    print('False')