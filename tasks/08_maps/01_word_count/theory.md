# Разбор задания

## Создание и запись

~~~go
counts := make(map[string]int)
for _, w := range strings.Fields(line) {
    counts[w]++
}
~~~

Если ключа нет, `counts[w]` возвращает нулевое значение `0`, поэтому `++`
работает сразу.

## Сортировка ключей

Порядок обхода `map` в Go **не определён**. Чтобы вывод был стабильным,
собери ключи в срез и отсортируй:

~~~go
keys := make([]string, 0, len(counts))
for k := range counts {
    keys = append(keys, k)
}
sort.Strings(keys)
~~~

## Печать

~~~go
for _, k := range keys {
    fmt.Printf("%s: %d\n", k, counts[k])
}
~~~
