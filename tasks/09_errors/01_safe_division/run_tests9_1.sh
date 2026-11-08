#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "10 2" $'Result: 5\n'
run_case "5 0" $'Error: division by zero\n'
run_case "-9 3" $'Result: -3\n'
run_case "0 7" $'Result: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
