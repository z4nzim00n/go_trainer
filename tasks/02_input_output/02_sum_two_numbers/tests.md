# GO_02_02. Сумма двух чисел — Тесты

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
| `2 3` | `5\n` |
| `-4 10` | `6\n` |
| `0 0` | `0\n` |
| `1000000 2000000` | `3000000\n` |

## Автотесты

```bash
bash run_tests2_2.sh
```
