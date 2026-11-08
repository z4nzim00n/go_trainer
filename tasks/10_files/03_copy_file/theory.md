# Разбор задания

## Копирование

~~~go
data, err := os.ReadFile(src)
if err != nil {
    fmt.Println("Error: cannot read source")
    return
}
err = os.WriteFile(dst, data, 0644)
~~~

Байты не нужно преобразовывать: `ReadFile` вернул `[]byte`, `WriteFile` его
принимает.

## Вывод содержимого

~~~go
fmt.Printf("Copied: %s\n", strings.TrimSpace(string(data)))
~~~

`TrimSpace` убирает пробелы и переводы строк по краям.

## Порядок проверок

Сначала читаем источник, потом пишем копию. Иначе при ошибке чтения можно
создать пустой файл назначения.
