#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "1234" $'4231\n'
run_case "12345" $'52341\n'
run_case "10" $'1\n'
run_case "99" $'99\n'
run_case "102" $'201\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
