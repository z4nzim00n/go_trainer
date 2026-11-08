# GO_12_05. Циклический сдвиг — Тесты

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
| `5 2\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `5 7\n1 2 3 4 5` | `4 5 1 2 3\n` |
| `1 3\n7` | `7\n` |
| `4 0\n1 2 3 4` | `1 2 3 4\n` |
| `0 5` | `\n` |

## Автотесты

```bash
bash run_tests12_5.sh
```
