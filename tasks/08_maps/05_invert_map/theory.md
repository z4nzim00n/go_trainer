# Разбор задания

## Инверсия

~~~go
direct := map[string]int{"a": 1, "b": 2}
inverse := make(map[int]string)
for word, num := range direct {
    inverse[num] = word
}
~~~

Ключи и значения меняются местами. Такая операция корректна, только если
значения уникальны.

## Числовая сортировка ключей

`sort.Strings` отсортировал бы `"10"` раньше `"5"`. Для чисел собираем срез
`[]int` и вызываем `sort.Ints`:

~~~go
nums := make([]int, 0, len(inverse))
for n := range inverse {
    nums = append(nums, n)
}
sort.Ints(nums)
~~~

## Вывод

~~~go
for _, n := range nums {
    fmt.Printf("%d: %s\n", n, inverse[n])
}
~~~
