# GO_05_03. Разворот среза — Тесты

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
| `5` + `1 2 3 4 5` | `5 4 3 2 1\n` |
| `4` + `10 20 30 40` | `40 30 20 10\n` |
| `1` + `7` | `7\n` |
| `0` | `\n` |

## Автотесты

```bash
bash run_tests5_3.sh
```
