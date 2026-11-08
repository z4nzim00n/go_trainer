#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "2.5 4" $'Area: 10.00\n'
run_case "1 1" $'Area: 1.00\n'
run_case "0 5" $'Area: 0.00\n'
run_case "3.5 2" $'Area: 7.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
