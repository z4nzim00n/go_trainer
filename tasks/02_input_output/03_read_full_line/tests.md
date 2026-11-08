# GO_02_03. Чтение строки целиком — Тесты

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
| `hello world` | `Line: hello world\n` |
| `Go is fun` | `Line: Go is fun\n` |
| *(пустая строка)* | `Line: \n` |
| `   ` | `Line:    \n` |

## Автотесты

```bash
bash run_tests2_3.sh
```
