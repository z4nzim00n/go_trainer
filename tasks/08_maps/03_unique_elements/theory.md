# Разбор задания

## Множество на map

В Go нет отдельного типа `set`. Его заменяет `map[T]bool`:

~~~go
seen := make(map[int]bool)
seen[3] = true
if seen[3] {
    // элемент уже встречался
}
~~~

## Сбор уникальных

~~~go
unique := make([]int, 0)
for _, x := range numbers {
    if !seen[x] {
        seen[x] = true
        unique = append(unique, x)
    }
}
sort.Ints(unique)
~~~

## Вывод среза

~~~go
parts := make([]string, len(unique))
for i, x := range unique {
    parts[i] = fmt.Sprint(x)
}
fmt.Println(strings.Join(parts, " "))
~~~
