#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "17" $'Prime\n'
run_case "9" $'Not prime\n'
run_case "1" $'Not prime\n'
run_case "2" $'Prime\n'
run_case "-5" $'Not prime\n'
run_case "97" $'Prime\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
