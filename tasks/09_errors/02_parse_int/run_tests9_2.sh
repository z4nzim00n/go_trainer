#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "42" $'Number: 42\n'
run_case "abc" $'Invalid number\n'
run_case "-7" $'Number: -7\n'
run_case "3.5" $'Invalid number\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
