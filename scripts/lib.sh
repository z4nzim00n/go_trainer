#!/usr/bin/env bash
# scripts/lib.sh — общие функции для run_tests.sh в заданиях Go-тренажёра.
#
# Источник решения задаётся переменной SOURCE_FILE (по умолчанию main.go):
#   SOURCE_FILE=solution.go bash run_tests1_1.sh
#
# Ожидаемый вывод в run_case — точные байты. Для переносов строк используй
# ANSI-C кавычки: run_case "2 2" $'4\n'  (Println)  или  run_case "2 2" "4"  (Print).
# Вывод программы нормализуется: \r\n -> \n (на Windows вывод тоже \n, но
# нормализация не мешает; на Linux/macOS в Школе 21 — \n).

# Портативный Go из tools/ имеет приоритет над системным.
# Ищем tools/go вверх по дереву от расположения lib.sh — это работает
# и из scripts/, и из рабочих копий.
_LIB_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
_source="$_LIB_DIR"
while :; do
  if [ -x "$_source/tools/go/bin/go.exe" ]; then
    export GOROOT="$_source/tools/go"
    export PATH="$GOROOT/bin:$PATH"
    export GOCACHE="$_source/tools/gocache"
    break
  fi
  if [ -x "$_source/tools/go/bin/go" ]; then
    export GOROOT="$_source/tools/go"
    export PATH="$GOROOT/bin:$PATH"
    export GOCACHE="$_source/tools/gocache"
    break
  fi
  _parent="$(dirname "$_source")"
  [ "$_parent" = "$_source" ] && break
  _source="$_parent"
done
unset _source _parent

# Сборка одного файла не требует go.mod.
export GO111MODULE=off

SOURCE_FILE="${SOURCE_FILE:-main.go}"
BUILD_DIR=".build"
case "$(uname -s)" in
  MINGW*|MSYS*|CYGWIN*) APP="$BUILD_DIR/app.exe" ;;
  *)                    APP="$BUILD_DIR/app" ;;
esac

# compile [доп. аргументы go build]
compile() {
  mkdir -p "$BUILD_DIR"
  go build -trimpath -o "$APP" "$SOURCE_FILE" "$@"
}

# Внутренний помощник: сравнивает /tmp/actual.out с ожидаемым значением.
_compare_and_report() {
  local label="$1" expected="$2"
  printf '%s' "$expected" > /tmp/expected.out
  if cmp -s /tmp/actual.out /tmp/expected.out; then
    echo "OK:   $label -> '$expected'"
  else
    echo "FAIL: $label -> получили '$(cat -A /tmp/actual.out)', ждали '$(cat -A /tmp/expected.out)'"
    FAILED=1
  fi
}

# run_case "вход" "ожидаемый_вывод" — вход через printf (добавляет \n)
run_case() {
  local input="$1" expected="$2"
  printf '%s\n' "$input" | "$APP" | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "'$input'" "$expected"
}

# run_case_noeol "вход" "ожидаемый_вывод" — вход БЕЗ завершающего \n
run_case_noeol() {
  local input="$1" expected="$2"
  printf '%s' "$input" | "$APP" | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "'$input' (без \\n)" "$expected"
}

# run_case_devnull "ожидаемый_вывод" — вход полностью пуст (EOF до первого символа)
run_case_devnull() {
  local expected="$1"
  "$APP" < /dev/null | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "(/dev/null)" "$expected"
}

# run_case_args "аргументы" "вход" "ожидаемый_вывод"
run_case_args() {
  local args="$1" input="$2" expected="$3"
  printf '%s\n' "$input" | "$APP" $args | tr -d '\r' > /tmp/actual.out || true
  _compare_and_report "args='$args' input='$input'" "$expected"
}
