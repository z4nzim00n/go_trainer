#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "4" $'Counter: 4000\n'
run_case "1" $'Counter: 1000\n'
run_case "0" $'Counter: 0\n'
run_case "3" $'Counter: 3000\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
