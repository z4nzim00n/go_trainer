# GO_12_03. Статистика — Тесты

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
| `3\n1 5 7` | `Min: 1\nMax: 7\nAvg: 4.33\n` |
| `0` | `Min: 0\nMax: 0\nAvg: 0.00\n` |
| `1\n5` | `Min: 5\nMax: 5\nAvg: 5.00\n` |
| `4\n-2 4 0 2` | `Min: -2\nMax: 4\nAvg: 1.00\n` |

## Автотесты

```bash
bash run_tests12_3.sh
```
