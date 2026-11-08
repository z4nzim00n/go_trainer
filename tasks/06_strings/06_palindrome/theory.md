# Разбор задания

## Нормализация

Собери новую последовательность только из букв и цифр, приведённых к нижнему
регистру:

~~~go
var normalized []rune
for _, r := range s {
    if unicode.IsLetter(r) || unicode.IsDigit(r) {
        normalized = append(normalized, unicode.ToLower(r))
    }
}
~~~

## Проверка

~~~go
ok := true
for i, j := 0, len(normalized)-1; i < j; i, j = i+1, j-1 {
    if normalized[i] != normalized[j] {
        ok = false
        break
    }
}
fmt.Println(ok)
~~~

## Пустая строка

Пустая строка (и строка только из знаков препинания) считается палиндромом:
сравнивать нечего, условие не нарушено.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| Сравнение без `ToLower` | `Aa` не считается палиндромом |
| Учёт пробелов | `a b a` ошибочно не палиндром |
| Разворот байтов | Ломает Unicode |
