# GO_13_01. Поля через reflection — Тесты

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
| `Alice 30` | `Name=Alice Age=30\n` |
| `Bob 0` | `Name=Bob Age=0\n` |
| `Eve -1` | `Name=Eve Age=-1\n` |

## Автотесты

```bash
bash run_tests13_1.sh
```
