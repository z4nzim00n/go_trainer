# GO_02_05. Число и строка — Тесты

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
| `Alice 30` | `Hello, Alice! You are 30.\n` |
| `Bob 7` | `Hello, Bob! You are 7.\n` |
| `Gopher 1` | `Hello, Gopher! You are 1.\n` |
| `X 0` | `Hello, X! You are 0.\n` |

## Автотесты

```bash
bash run_tests2_5.sh
```
