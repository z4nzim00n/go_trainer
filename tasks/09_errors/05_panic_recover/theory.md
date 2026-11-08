# Разбор задания

## panic

~~~go
panic("division by zero")
~~~

Паника останавливает обычное выполнение и раскручивает стек.

## recover

~~~go
func SafeDivide(a, b int) (result int, err error) {
    defer func() {
        if r := recover(); r != nil {
            err = fmt.Errorf("%v", r)
        }
    }()
    if b == 0 {
        panic("division by zero")
    }
    return a / b, nil
}
~~~

`recover` работает только внутри `defer`. Он возвращает значение паники
или `nil`, если паники не было.

## Именованный результат

`(result int, err error)` позволяет `defer` записать значение в `err` после
возврата из функции.

## Важно

`panic` — не замена ошибкам. В обычном коде возвращай `error`, а `recover`
используй на границах программы.
