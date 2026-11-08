# GO_09_02. Разбор числа — Тесты

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
| `42` | `Number: 42\n` |
| `abc` | `Invalid number\n` |
| `-7` | `Number: -7\n` |
| `3.5` | `Invalid number\n` |

## Автотесты

```bash
bash run_tests9_2.sh
```
