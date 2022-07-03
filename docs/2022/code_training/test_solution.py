#!/usr/bin/env python3

import sys
import traceback

if __name__ == '__main__':
    mod_name = 'test_module'
    if len(sys.argv) < 2:
        print(f'USAGE: {sys.argv[0]} <function_call>')
        print(f"The module '{mod_name}.py' is assumed to exist "\
              'and it to have the class \'Solution\' defined.')
        exit(1)
    
    imp_str = f"import {mod_name} as lc"
    obj_str = "s = lc.Solution()"
    f_name = sys.argv[1]
    args = ','.join(sys.argv[2:])
    input_str = '\n'.join(sys.argv[2:])
    ans_str = f"ans = s.{f_name}({args})"
    
    print('----stdout----')
    for cmd in [imp_str, obj_str, ans_str]:
        try:
            exec(cmd)
        except Exception as e:
            print(f"\nCouldn't run: '{cmd}'\n")
            print(traceback.format_exc())
            exit(1)
        
    print('--------------')

    print('----input-----')
    print(input_str)
    print('----answer----')
    print(str(ans))
    exit(0)
