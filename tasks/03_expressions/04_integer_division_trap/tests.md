# GO_03_04. Ловушка целочисленного деления — Тесты

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
| `3 4` | `Avg: 3.50\n` |
| `1 2` | `Avg: 1.50\n` |
| `-3 4` | `Avg: 0.50\n` |
| `5 5` | `Avg: 5.00\n` |

## Автотесты

```bash
bash run_tests3_4.sh
```
