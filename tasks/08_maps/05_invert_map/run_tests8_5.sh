#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'3\na 1\nb 2\nc 3' $'1: a\n2: b\n3: c\n'
run_case $'2\nz 10\ny 5' $'5: y\n10: z\n'
run_case $'1\nsolo 42' $'42: solo\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
