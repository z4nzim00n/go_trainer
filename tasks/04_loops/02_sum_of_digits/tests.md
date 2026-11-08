# GO_04_02. Сумма цифр — Тесты

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
| `12345` | `15\n` |
| `0` | `0\n` |
| `9999` | `36\n` |
| `7` | `7\n` |
| `1000` | `1\n` |
| `2000000000` | `2\n` |

## Автотесты

```bash
bash run_tests4_2.sh
```
