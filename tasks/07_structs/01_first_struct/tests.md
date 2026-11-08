# GO_07_01. Первая структура — Тесты

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
| `3 4` | `X: 3\nY: 4\n` |
| `-1 0` | `X: -1\nY: 0\n` |
| `0 0` | `X: 0\nY: 0\n` |

## Автотесты

```bash
bash run_tests7_1.sh
```
