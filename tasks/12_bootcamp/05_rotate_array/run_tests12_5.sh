#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5 2\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'5 7\n1 2 3 4 5' $'4 5 1 2 3\n'
run_case $'1 3\n7' $'7\n'
run_case $'4 0\n1 2 3 4' $'1 2 3 4\n'
run_case "0 5" $'\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
