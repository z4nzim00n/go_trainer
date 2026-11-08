# Разбор задания

## fmt.Stringer

~~~go
type Stringer interface {
    String() string
}
~~~

Если у типа есть метод `String() string`, `fmt` использует его при печати
через `%v`, `%s` и `Println`.

## Свой тип на основе float64

~~~go
type Temperature float64

func (t Temperature) String() string {
    return fmt.Sprintf("%.2f°C", float64(t))
}
~~~

Внутри метода приводим `t` к `float64`, потому что `Sprintf` ожидает обычное
число.

## Печать

~~~go
fmt.Printf("Temp: %v\n", t)
~~~

`%v` вызовет `String()` автоматически.
