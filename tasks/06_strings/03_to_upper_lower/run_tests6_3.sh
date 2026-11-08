#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
source ../../../scripts/lib.sh

compile

run_case $'hello\nWORLD' $'HELLO\nworld\n'
run_case $'Go\nLang' $'GO\nlang\n'
run_case $'\n' $'\n\n'

if [ -z "$FAILED" ]; then
  echo "Все тесты пройдены"
else
  echo "Есть проваленные тесты"
  exit 1
fi
