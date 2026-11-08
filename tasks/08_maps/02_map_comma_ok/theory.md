# Разбор задания

## Проблема нулевого значения

~~~go
v := m["missing"] // v == 0
~~~

Нельзя понять, лежит в map ноль или ключа вообще нет.

## Идиома comma-ok

~~~go
v, ok := m["dog"]
if ok {
    fmt.Println(v)
} else {
    fmt.Println("NOT FOUND")
}
~~~

Второе значение — `bool`: был ли ключ найден.

## Чтение пар

~~~go
m := make(map[string]int)
for i := 0; i < n; i++ {
    var key string
    var value int
    fmt.Scan(&key, &value)
    m[key] = value
}
~~~
