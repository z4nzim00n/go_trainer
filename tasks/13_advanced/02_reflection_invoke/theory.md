# Разбор задания

## Поиск метода

~~~go
c := Calculator{}
m := reflect.ValueOf(c).MethodByName("Add")
~~~

`MethodByName` возвращает `reflect.Value`, который можно вызвать.

## Call

~~~go
args := []reflect.Value{
    reflect.ValueOf(a),
    reflect.ValueOf(b),
}
out := m.Call(args)
~~~

`Call` принимает срез значений и возвращает срез результатов.

## Результат

~~~go
fmt.Println(out[0].Int())
~~~

Для `int` используем `Int()`, для `string` — `String()`, для `float64` —
`Float()`.

## Осторожно

Если метода нет, `MethodByName` вернёт нулевое значение, а `Call` запаникует.
В реальном коде проверяй `m.IsValid()`.
