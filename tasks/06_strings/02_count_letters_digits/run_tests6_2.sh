#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Hello123" $'5 3\n'
run_case "abc" $'3 0\n'
run_case "12345" $'0 5\n'
run_case "a1b2c3" $'3 3\n'
run_case "!?.," $'0 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
