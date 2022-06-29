#!/usr/bin/env python3
import sys
if __name__ == '__main__':
    mod_name = 'test_module'
    if len(sys.argv) < 2:
        print(f'USAGE: {sys.argv[0]} <function> {{args,}}')
        print(f"The module '{mod_name}.py' is assumed to exist "\
              'and to have the class \'Solution\' defined.')
        exit(1)
    
    imp_str = f"import {mod_name} as lc"
    obj_str = "s = lc.Solution()"
    ans_str = f"ans = s.{sys.argv[1]}({','.join(sys.argv[2:])})"
    inp_str = '\n'.join(sys.argv[2:])
    
    print('----stdout----')
    exec(imp_str)
    exec(obj_str)
    exec(ans_str)


    print('\n----input-----')
    print(inp_str)
    print('----answer----')
    print(str(ans))
    exit(0)
