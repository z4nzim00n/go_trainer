#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "42" $'int: 42\n'
run_case "3.5" $'float: 3.50\n'
run_case "hello" $'string: hello\n'
run_case "-7" $'int: -7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
