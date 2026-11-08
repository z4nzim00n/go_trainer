# GO_09_05. panic и recover — Тесты

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
| `10 2` | `Result: 5\n` |
| `5 0` | `Recovered: division by zero\n` |
| `0 4` | `Result: 0\n` |
| `-8 2` | `Result: -4\n` |

## Автотесты

```bash
bash run_tests9_5.sh
```
