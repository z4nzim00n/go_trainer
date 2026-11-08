#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3 5" $'5 3\n'
run_case "-1 7" $'7 -1\n'
run_case "0 0" $'0 0\n'
run_case "42 42" $'42 42\n'
run_case $'3\n5' $'5 3\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
