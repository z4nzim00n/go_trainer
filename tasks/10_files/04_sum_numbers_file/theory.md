# Разбор задания

## Разбор файла

~~~go
data, err := os.ReadFile(name)
if err != nil {
    fmt.Println("Error: cannot read file")
    return
}
fields := strings.Fields(string(data))
~~~

`Fields` разбивает по любым пробельным символам, поэтому числа могут быть
на разных строках.

## Преобразование и сумма

~~~go
sum := 0
for _, f := range fields {
    n, err := strconv.Atoi(f)
    if err != nil {
        continue
    }
    sum += n
}
fmt.Printf("Sum: %d\n", sum)
~~~

## Крайний случай

Для пустого файла `Fields` вернёт пустой срез, цикл не выполнится, сумма
останется `0`.
