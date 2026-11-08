# GO_09_03. Своя ошибка — Тесты

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
| `-1` | `Validation error: age\n` |
| `20` | `Age: 20\n` |
| `0` | `Age: 0\n` |
| `-100` | `Validation error: age\n` |

## Автотесты

```bash
bash run_tests9_3.sh
```
