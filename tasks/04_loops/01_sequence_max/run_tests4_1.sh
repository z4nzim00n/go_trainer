#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 9 -2 9 0' $'9\n'
run_case $'1\n-42' $'-42\n'
run_case $'4\n-5 -1 -9 -3' $'-1\n'
run_case $'3\n7 7 7' $'7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
