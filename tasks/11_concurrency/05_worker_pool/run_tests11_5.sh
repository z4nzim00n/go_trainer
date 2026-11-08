#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "5" $'Total: 55\n'
run_case "3" $'Total: 14\n'
run_case "0" $'Total: 0\n'
run_case "10" $'Total: 385\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
