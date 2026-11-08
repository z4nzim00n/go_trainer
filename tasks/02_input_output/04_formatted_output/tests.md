# GO_02_04. Форматированный вывод — Тесты

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
| `3.14159` | `Value: 3.14\n` |
| `2` | `Value: 2.00\n` |
| `-0.5` | `Value: -0.50\n` |
| `0` | `Value: 0.00\n` |

## Автотесты

```bash
bash run_tests2_4.sh
```
