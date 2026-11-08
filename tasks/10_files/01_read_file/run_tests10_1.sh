#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f f1.txt missing.txt' EXIT
printf 'hello\nworld\n' > f1.txt
run_case "f1.txt" $'hello\nworld\n'
printf 'abc' > f1.txt
run_case "f1.txt" "abc"
run_case "missing.txt" $'Error: cannot read file\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
