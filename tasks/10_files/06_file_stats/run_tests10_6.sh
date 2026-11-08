#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

trap 'rm -f f.txt empty.txt' EXIT
printf 'a\nb\n' > f.txt
run_case "f.txt" $'Lines: 2\nBytes: 4\n'
: > empty.txt
run_case "empty.txt" $'Lines: 0\nBytes: 0\n'
printf 'hello' > f.txt
run_case "f.txt" $'Lines: 1\nBytes: 5\n'
printf 'x\ny' > f.txt
run_case "f.txt" $'Lines: 2\nBytes: 3\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
