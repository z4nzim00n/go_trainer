#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'5\n3 9 -2 9 0' $'Min: -2\nMax: 9\n'
run_case $'1\n-42' $'Min: -42\nMax: -42\n'
run_case $'4\n-5 -1 -9 -3' $'Min: -9\nMax: -1\n'
run_case $'3\n7 7 7' $'Min: 7\nMax: 7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
