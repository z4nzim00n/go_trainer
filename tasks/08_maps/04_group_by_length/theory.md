# Разбор задания

## Map со срезом в значении

~~~go
groups := make(map[int][]string)
for _, w := range words {
    n := len([]rune(w))
    groups[n] = append(groups[n], w)
}
~~~

Значение map — срез, поэтому `append` дописывает слово в нужную группу.

## Сортировка

~~~go
lengths := make([]int, 0, len(groups))
for n := range groups {
    lengths = append(lengths, n)
}
sort.Ints(lengths)
for _, n := range lengths {
    sort.Strings(groups[n])
}
~~~

## Длина в рунах

`len(w)` считает байты. Для кириллицы правильнее `len([]rune(w))`.
