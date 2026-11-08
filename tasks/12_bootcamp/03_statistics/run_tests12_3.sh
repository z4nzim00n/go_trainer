#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\n1 5 7' $'Min: 1\nMax: 7\nAvg: 4.33\n'
run_case "0" $'Min: 0\nMax: 0\nAvg: 0.00\n'
run_case $'1\n5' $'Min: 5\nMax: 5\nAvg: 5.00\n'
run_case $'4\n-2 4 0 2' $'Min: -2\nMax: 4\nAvg: 1.00\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
