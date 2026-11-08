#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5 2\n1 2 3 4 5' $'3 4 5 1 2\n'
run_case $'4 0\n1 2 3 4' $'1 2 3 4\n'
run_case $'3 4\n7 8 9' $'8 9 7\n'
run_case $'1 5\n42' $'42\n'
run_case $'5 7\n1 2 3 4 5' $'3 4 5 1 2\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
