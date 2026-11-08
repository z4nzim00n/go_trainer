# GO_04_03. Максимальная цифра — Тесты

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
| `2739` | `9\n` |
| `0` | `0\n` |
| `1111` | `1\n` |
| `907` | `9\n` |
| `1234567890` | `9\n` |
| `-907` | `9\n` |

## Автотесты

```bash
bash run_tests4_3.sh
```
