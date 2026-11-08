#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3.14159" $'Value: 3.14\n'
run_case "2" $'Value: 2.00\n'
run_case "-0.5" $'Value: -0.50\n'
run_case "0" $'Value: 0.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
