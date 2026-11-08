# Разбор задания

## Метод

~~~go
type Rectangle struct {
    Width  float64
    Height float64
}

func (r Rectangle) Area() float64 {
    return r.Width * r.Height
}
~~~

`(r Rectangle)` — получатель. Внутри метода поля доступны как `r.Width`.

## Вызов

~~~go
r := Rectangle{Width: 2.5, Height: 4}
fmt.Printf("Area: %.2f\n", r.Area())
~~~

`%.2f` печатает число с двумя знаками после запятой.

## Указатель или значение

Для метода, который только читает поля, достаточно получателя-значения.
Получатель-указатель `(r *Rectangle)` нужен, если метод меняет структуру.
