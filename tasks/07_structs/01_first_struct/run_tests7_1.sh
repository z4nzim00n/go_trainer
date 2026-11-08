#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "3 4" $'X: 3\nY: 4\n'
run_case "-1 0" $'X: -1\nY: 0\n'
run_case "0 0" $'X: 0\nY: 0\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
