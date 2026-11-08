# GO_06_02. Буквы и цифры — Тесты

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
| `Hello123` | `5 3\n` |
| `abc` | `3 0\n` |
| `12345` | `0 5\n` |
| `a1b2c3` | `3 3\n` |
| `!?.,` | `0 0\n` |

## Автотесты

```bash
bash run_tests6_2.sh
```
