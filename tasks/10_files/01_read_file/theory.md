# Разбор задания

## os.ReadFile

~~~go
data, err := os.ReadFile(name)
if err != nil {
    fmt.Println("Error: cannot read file")
    return
}
fmt.Print(string(data))
~~~

Функция возвращает `[]byte`. `string(data)` превращает байты в строку.

## Print или Println

- `fmt.Print` — без добавления перевода строки;
- `fmt.Println` — добавляет `\n`.

Если файл уже заканчивается переводом строки, `Print` сохранит его как есть.

## Учебные файлы в тестах

Автотест создаёт `f1.txt` командой `printf` и передаёт его имя программе.
