#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\n1 2 3' $'Sum: 6\nAvg: 2.00\n'
run_case $'1\n5' $'Sum: 5\nAvg: 5.00\n'
run_case "0" $'Sum: 0\nAvg: 0.00\n'
run_case $'4\n-2 4 0 2' $'Sum: 4\nAvg: 1.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
