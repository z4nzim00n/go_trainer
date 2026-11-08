# GO_09_01. Безопасное деление — Тесты

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
| `10 2` | `Result: 5\n` |
| `5 0` | `Error: division by zero\n` |
| `-9 3` | `Result: -3\n` |
| `0 7` | `Result: 0\n` |

## Автотесты

```bash
bash run_tests9_1.sh
```
