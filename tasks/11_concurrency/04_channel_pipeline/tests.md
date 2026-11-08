# GO_11_04. Конвейер каналов — Тесты

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
| `3\n1 2 3` | `Sum: 14\n` |
| `2\n2 4` | `Sum: 20\n` |
| `0` | `Sum: 0\n` |
| `4\n1 1 1 1` | `Sum: 4\n` |

## Автотесты

```bash
bash run_tests11_4.sh
```
