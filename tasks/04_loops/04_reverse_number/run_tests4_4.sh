#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "12340" $'4321\n'
run_case "0" $'0\n'
run_case "100" $'1\n'
run_case "7" $'7\n'
run_case "1234567899" $'9987654321\n'
run_case "-123" $'321\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
