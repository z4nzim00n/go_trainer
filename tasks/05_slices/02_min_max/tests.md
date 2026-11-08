# GO_05_02. Минимум и максимум — Тесты

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
| `5` + `3 9 -2 9 0` | `Min: -2\nMax: 9\n` |
| `1` + `-42` | `Min: -42\nMax: -42\n` |
| `4` + `-5 -1 -9 -3` | `Min: -9\nMax: -1\n` |
| `3` + `7 7 7` | `Min: 7\nMax: 7\n` |

## Автотесты

```bash
bash run_tests5_2.sh
```
