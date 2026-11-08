#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n5 1 4 2 3' $'1 2 3 4 5\n'
run_case $'4\n-1 3 -5 0' $'-5 -1 0 3\n'
run_case $'3\n7 7 1' $'1 7 7\n'
run_case "0" $'\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
