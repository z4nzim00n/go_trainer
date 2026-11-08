# Разбор задания

## interface{}

~~~go
var v interface{}
v = 42        // int
v = 3.5       // float64
v = "hello"   // string
~~~

В `interface{}` (синоним `any`) можно положить значение любого типа.

## Type switch

~~~go
switch x := v.(type) {
case int:
    fmt.Printf("int: %d\n", x)
case float64:
    fmt.Printf("float: %.2f\n", x)
case string:
    fmt.Printf("string: %s\n", x)
}
~~~

В каждой ветке `x` уже имеет конкретный тип.

## Определение типа по строке

~~~go
if n, err := strconv.Atoi(s); err == nil {
    v = n
} else if f, err := strconv.ParseFloat(s, 64); err == nil {
    v = f
} else {
    v = s
}
~~~

Сначала пробуем целое, потом дробное, иначе оставляем строку.

## Частые ошибки

| Ошибка | Что происходит |
| --- | --- |
| `case float:` | Такого типа нет, нужен `float64` |
| Сравнение типов через `==` | Нужен type switch или `reflect` |
| `x` вне switch | Переменная из `case` видна только в ветке |
