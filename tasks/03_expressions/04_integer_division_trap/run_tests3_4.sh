#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3 4" $'Avg: 3.50\n'
run_case "1 2" $'Avg: 1.50\n'
run_case "-3 4" $'Avg: 0.50\n'
run_case "5 5" $'Avg: 5.00\n'
run_case $'2\n3' $'Avg: 2.50\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
