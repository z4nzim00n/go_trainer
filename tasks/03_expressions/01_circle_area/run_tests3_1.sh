#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "1" $'Area: 3.14\n'
run_case "2" $'Area: 12.57\n'
run_case "0" $'Area: 0.00\n'
run_case "2.5" $'Area: 19.63\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
