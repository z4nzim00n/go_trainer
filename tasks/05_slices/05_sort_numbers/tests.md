# GO_05_05. Сортировка чисел — Тесты

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
| `5` + `5 1 4 2 3` | `1 2 3 4 5\n` |
| `4` + `-1 3 -5 0` | `-5 -1 0 3\n` |
| `3` + `7 7 1` | `1 7 7\n` |
| `0` | `\n` |

## Автотесты

```bash
bash run_tests5_5.sh
```
