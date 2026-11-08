# GO_12_06. Сумма матрицы — Тесты

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
| `2 3\n1 2 3\n4 5 6` | `Sum: 21\n` |
| `1 1\n7` | `Sum: 7\n` |
| `0 0` | `Sum: 0\n` |
| `3 2\n-1 2\n3 4\n5 -6` | `Sum: 7\n` |

## Автотесты

```bash
bash run_tests12_6.sh
```
