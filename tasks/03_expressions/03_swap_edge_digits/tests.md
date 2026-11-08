# GO_03_03. Перестановка крайних цифр — Тесты

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
| `1234` | `4231\n` |
| `12345` | `52341\n` |
| `10` | `1\n` |
| `99` | `99\n` |
| `102` | `201\n` |

## Автотесты

```bash
bash run_tests3_3.sh
```
