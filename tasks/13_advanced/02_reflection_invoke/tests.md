# GO_13_02. Вызов метода через reflection — Тесты

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
| `2 3` | `Result: 5\n` |
| `-1 1` | `Result: 0\n` |
| `10 20` | `Result: 30\n` |

## Автотесты

```bash
bash run_tests13_2.sh
```
