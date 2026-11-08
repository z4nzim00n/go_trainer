# Разбор задания

## Интерфейс

~~~go
type Shape interface {
    Area() float64
}
~~~

Тип реализует интерфейс, если у него есть все методы интерфейса. Слово
`implements` писать не нужно.

## Две реализации

~~~go
type Circle struct{ R float64 }
func (c Circle) Area() float64 { return math.Pi * c.R * c.R }

type Square struct{ Side float64 }
func (s Square) Area() float64 { return s.Side * s.Side }
~~~

## Полиморфизм

~~~go
shapes := []Shape{Circle{R: 2}, Square{Side: 3}}
total := 0.0
for _, s := range shapes {
    total += s.Area()
}
~~~

Цикл вызывает `Area` у конкретного типа, лежащего в переменной интерфейса.
