#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'2 3\n1 2 3\n4 5 6' $'Sum: 21\n'
run_case $'1 1\n7' $'Sum: 7\n'
run_case "0 0" $'Sum: 0\n'
run_case $'3 2\n-1 2\n3 4\n5 -6' $'Sum: 7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
