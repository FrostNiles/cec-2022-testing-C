import runpy
import re
import sys

skipped = {6}
for i in range(12, 13):
    # CEC 2022 has 12 functions
    if i in skipped:
        continue
    for j in [10, 20]:
        for k in range(j, j+1):
            args = {
                'arg1': str(i),
                'arg2': str(j),
                'arg3': str(k)
            }
            
            runpy.run_path('./run-tests.py', init_globals=args)


