#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "Alice 30" $'Hello, Alice! You are 30.\n'
run_case "Bob 7" $'Hello, Bob! You are 7.\n'
run_case "Gopher 1" $'Hello, Gopher! You are 1.\n'
run_case "X 0" $'Hello, X! You are 0.\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
