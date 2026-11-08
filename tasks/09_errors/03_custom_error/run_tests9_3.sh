#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "-1" $'Validation error: age\n'
run_case "20" $'Age: 20\n'
run_case "0" $'Age: 0\n'
run_case "-100" $'Validation error: age\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
