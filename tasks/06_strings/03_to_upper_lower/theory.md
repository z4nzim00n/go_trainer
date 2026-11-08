# Разбор задания

## Пакет strings

~~~go
import "strings"

upper := strings.ToUpper(first)
lower := strings.ToLower(second)
~~~

`ToUpper` и `ToLower` возвращают **новую** строку: строки в Go неизменяемы.

## Чтение двух строк

~~~go
scanner := bufio.NewScanner(os.Stdin)
scanner.Scan()
first := scanner.Text()
scanner.Scan()
second := scanner.Text()
~~~

Каждый `Scan` читает одну строку. Проверять результат нужно, если ввод может
закончиться раньше.

## Unicode

`strings.ToUpper` корректно работает с Unicode, а не только с латиницей.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `strings.ToUpper` без импорта | Ошибка компиляции |
| `fmt.Scan` для строк с пробелами | Читается только первое слово |
| Перепутаны строки | Неверный порядок вывода |
