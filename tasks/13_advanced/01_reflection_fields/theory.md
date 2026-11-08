# Разбор задания

## reflect.Type и reflect.Value

~~~go
v := reflect.ValueOf(p)
t := v.Type()
fmt.Println(t.NumField())
~~~

`reflect.TypeOf` и `reflect.ValueOf` дают описание типа и значения во время
выполнения.

## Обход полей

~~~go
for i := 0; i < t.NumField(); i++ {
    field := t.Field(i)
    value := v.Field(i)
    fmt.Println(field.Name, value.Interface())
}
~~~

`Field(i)` у типа возвращает метаданные, у значения — само значение.

## Interface()

`value.Interface()` возвращает значение как `interface{}`, чтобы его можно
было напечатать через `%v`.

## Когда нужно

Reflection пригодится для сериализации, валидации и обобщённых библиотек.
В обычном коде старайся обходиться без него: он медленнее и менее безопасен.
