# GO_13_04. Обобщённый Max — Тесты

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
| `2.5 7.5` | `Max: 7.50\n` |
| `-1 -2` | `Max: -1.00\n` |
| `3 3` | `Max: 3.00\n` |

## Автотесты

```bash
bash run_tests13_4.sh
```
