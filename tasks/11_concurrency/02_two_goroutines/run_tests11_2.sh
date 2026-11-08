#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3 4" $'Sum: 14\n'
run_case "0 5" $'Sum: 10\n'
run_case "-1 2" $'Sum: 2\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
