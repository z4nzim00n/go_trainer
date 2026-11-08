# GO_05_04. Удаление дубликатов — Тесты

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
| `6` + `1 2 1 3 2 4` | `1 2 3 4\n` |
| `4` + `3 1 3 2` | `3 1 2\n` |
| `5` + `5 5 5 5 5` | `5\n` |
| `0` | `\n` |

## Автотесты

```bash
bash run_tests5_4.sh
```
