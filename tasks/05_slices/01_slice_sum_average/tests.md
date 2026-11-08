# GO_05_01. Сумма и среднее — Тесты

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
| `3` + `1 2 3` | `Sum: 6\nAvg: 2.00\n` |
| `1` + `5` | `Sum: 5\nAvg: 5.00\n` |
| `0` | `Sum: 0\nAvg: 0.00\n` |
| `4` + `-2 4 0 2` | `Sum: 4\nAvg: 1.00\n` |

## Автотесты

```bash
bash run_tests5_1.sh
```
