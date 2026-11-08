# GO_11_05. Пул воркеров — Тесты

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
| `5` | `Total: 55\n` |
| `3` | `Total: 14\n` |
| `0` | `Total: 0\n` |
| `10` | `Total: 385\n` |

## Автотесты

```bash
bash run_tests11_5.sh
```
