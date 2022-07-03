#!/bin/bash

if [[ $# -lt 2 ]]; then
    echo "USAGE: ./$(basename $0) <module-to-test> <function> {args,}"
    exit 1
fi
org_mod="$1"
tmp_mod=test_module.py
echo cp $org_mod $tmp_mod
cp $org_mod $tmp_mod
shift
python3 test_solution.py $@
#rm -f $tmp_mod
