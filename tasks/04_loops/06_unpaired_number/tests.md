# GO_04_06. Число без пары — Тесты

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
| `5` + `1 2 3 2 1` | `3\n` |
| `3` + `4 4 -7` | `-7\n` |
| `1` + `42` | `42\n` |
| `5` + `8 8 0 0 5` | `5\n` |

## Автотесты

```bash
bash run_tests4_6.sh
```
