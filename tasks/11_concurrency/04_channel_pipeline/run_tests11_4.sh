#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\n1 2 3' $'Sum: 14\n'
run_case $'2\n2 4' $'Sum: 20\n'
run_case "0" $'Sum: 0\n'
run_case $'4\n1 1 1 1' $'Sum: 4\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
