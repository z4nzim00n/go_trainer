#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case "apple banana apple" $'apple: 2\nbanana: 1\n'
run_case "a" $'a: 1\n'
run_case "b a b a b" $'a: 2\nb: 3\n'
run_case "" ""

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
