# Разбор задания

## Свой тип ошибки

~~~go
type ValidationError struct {
    Field string
}

func (e *ValidationError) Error() string {
    return "validation failed: " + e.Field
}
~~~

Любой тип с методом `Error() string` является ошибкой.

## Возврат

~~~go
func ValidateAge(age int) error {
    if age < 0 {
        return &ValidationError{Field: "age"}
    }
    return nil
}
~~~

Возвращаем указатель, потому что метод объявлен на `*ValidationError`.

## Достать конкретный тип

~~~go
var ve *ValidationError
if errors.As(err, &ve) {
    fmt.Println("Validation error:", ve.Field)
}
~~~

`errors.As` ищет ошибку нужного типа в цепочке обёрнутых ошибок.
