#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "2.5 7.5" $'Max: 7.50\n'
run_case "-1 -2" $'Max: -1.00\n'
run_case "3 3" $'Max: 3.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
