# Разбор задания

## os.WriteFile

~~~go
content := line + "\n"
err := os.WriteFile(name, []byte(content), 0644)
~~~

Третий аргумент — права доступа (как в Unix). `0644` означает: владелец
читает и пишет, остальные только читают.

`[]byte(content)` превращает строку в срез байтов.

## Проверка ошибки

~~~go
if err != nil {
    fmt.Println("Error: cannot write file")
    return
}
~~~

## Чтение обратно

~~~go
data, err := os.ReadFile(name)
fmt.Println("Saved: " + strings.TrimSpace(string(data)))
~~~

`TrimSpace` убирает перевод строки, который мы сами записали.
