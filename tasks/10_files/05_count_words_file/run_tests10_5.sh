#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f text.txt empty.txt' EXIT
printf 'one two\nthree\n' > text.txt
run_case "text.txt" $'Words: 3\n'
: > empty.txt
run_case "empty.txt" $'Words: 0\n'
printf 'a' > text.txt
run_case "text.txt" $'Words: 1\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
