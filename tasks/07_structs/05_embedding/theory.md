# Разбор задания

## Встраивание

~~~go
type Person struct {
    Name string
}

type Employee struct {
    Person
    Company string
}
~~~

Поле `Person` записано без имени — это встраивание (embedding).

## Продвижение полей

~~~go
e := Employee{Person: Person{Name: "Bob"}, Company: "Acme"}
fmt.Println(e.Name)      // Bob
fmt.Println(e.Person.Name) // тоже Bob
~~~

Поле `Name` «продвигается» наверх: к нему можно обращаться напрямую.

## Зачем это нужно

Встраивание заменяет наследование: `Employee` получает поля и методы
`Person`, но остаётся отдельным типом.
