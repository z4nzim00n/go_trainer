#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f numbers.txt empty.txt' EXIT
printf '1 2 3\n' > numbers.txt
run_case "numbers.txt" $'Sum: 6\n'
: > empty.txt
run_case "empty.txt" $'Sum: 0\n'
printf '10\n-5\n2' > numbers.txt
run_case "numbers.txt" $'Sum: 7\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
