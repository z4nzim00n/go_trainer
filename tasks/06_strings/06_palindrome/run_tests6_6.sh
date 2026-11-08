#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "A man, a plan, a canal: Panama" $'true\n'
run_case "hello" $'false\n'
run_case "12321" $'true\n'
run_case "" $'true\n'
run_case "No lemon, no melon" $'true\n'
run_case "abc" $'false\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
