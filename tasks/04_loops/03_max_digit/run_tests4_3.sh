#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "2739" $'9\n'
run_case "0" $'0\n'
run_case "1111" $'1\n'
run_case "907" $'9\n'
run_case "1234567890" $'9\n'
run_case "-907" $'9\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
