# GO_07_02. Метод Area — Тесты

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
| `2.5 4` | `Area: 10.00\n` |
| `1 1` | `Area: 1.00\n` |
| `0 5` | `Area: 0.00\n` |
| `3.5 2` | `Area: 7.00\n` |

## Автотесты

```bash
bash run_tests7_2.sh
```
