# GO_06_01. Длина строки — Тесты

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
| `Hello` | `5\n` |
| *(пустая строка)* | `0\n` |
| `   ` | `3\n` |
| `golang` | `6\n` |

## Автотесты

```bash
bash run_tests6_1.sh
```
