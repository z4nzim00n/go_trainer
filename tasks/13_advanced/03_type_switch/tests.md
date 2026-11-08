# GO_13_03. Type switch — Тесты

## Компиляция

```bash
go build -o app.exe main.go
./app.exe
```

Эталон:

```bash
go run solution.go
go run solution_commented.go
```

## Проверка вывода

| Вход | Результат |
| --- | --- |
| `42` | `int: 42\n` |
| `3.5` | `float: 3.50\n` |
| `hello` | `string: hello\n` |
| `-7` | `int: -7\n` |

## Автотесты

```bash
bash run_tests13_3.sh
```
