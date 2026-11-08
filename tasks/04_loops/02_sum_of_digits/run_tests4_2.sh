#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "12345" $'15\n'
run_case "0" $'0\n'
run_case "9999" $'36\n'
run_case "7" $'7\n'
run_case "1000" $'1\n'
run_case "2000000000" $'2\n'
run_case "-123" $'6\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
