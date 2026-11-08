# GO_01_05. Обмен значений — Тесты

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
| `3 5` | `5 3\n` |
| `-1 7` | `7 -1\n` |
| `0 0` | `0 0\n` |
| `42 42` | `42 42\n` |

## Автотесты

```bash
bash run_tests1_5.sh
```
