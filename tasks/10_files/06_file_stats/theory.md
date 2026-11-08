# Разбор задания

## Байты

~~~go
data, err := os.ReadFile(name)
fmt.Println(len(data))
~~~

`len([]byte)` — количество байтов. Для ASCII один символ равен одному байту,
для кириллицы — двум.

## Строки

~~~go
text := string(data)
text = strings.TrimSuffix(text, "\n")
lines := 0
if text != "" {
    lines = len(strings.Split(text, "\n"))
}
~~~

Сначала убираем последний перевод строки, чтобы `a\nb\n` дало две строки,
а не три. Пустой файл обрабатываем отдельно.

## Альтернатива

~~~go
lines := strings.Count(string(data), "\n")
if len(data) > 0 && !strings.HasSuffix(string(data), "\n") {
    lines++
}
~~~
