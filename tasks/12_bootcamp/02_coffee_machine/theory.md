# Разбор задания

## Накопление

~~~go
total := 0
for i := 0; i < n; i++ {
    var coin int
    fmt.Scan(&coin)
    total += coin
}
~~~

## Ветвление

~~~go
const price = 50
if total >= price {
    fmt.Printf("Coffee: %d\n", total-price)
} else {
    fmt.Printf("Need: %d\n", price-total)
}
~~~

`const` объявляет неизменяемую константу.

## Точное равенство

Случай `total == 50` попадает в первую ветку: сдача `0`. Проверяй границу
явно — это классическая ошибка `>` вместо `>=`.
