# Разбор задания

## Обход рун

~~~go
for _, r := range s {
    if unicode.IsLetter(r) {
        letters++
    }
    if unicode.IsDigit(r) {
        digits++
    }
}
~~~

`range` по строке возвращает **руны**, а не байты — это важно для кириллицы.

## Проверки Unicode

| Функция | Что считает буквой/цифрой |
| --- | --- |
| `unicode.IsLetter` | любые буквы Unicode |
| `unicode.IsDigit` | десятичные цифры |
| `unicode.IsSpace` | пробелы, табы, переводы строк |

Для ASCII есть `r >= 'a' && r <= 'z'`, но Unicode-функции универсальнее.

## Вывод

~~~go
fmt.Printf("%d %d\n", letters, digits)
~~~

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `for i := 0; i < len(s); i++` | Обход байтов, кириллица ломается |
| `r >= '0' && r <= '9'` | Работает только для ASCII-цифр |
| `IsNumber` вместо `IsDigit` | Считает и римские цифры |
