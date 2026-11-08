# GO_07_05. Встраивание структур — Тесты

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
| `Bob Acme` | `Name: Bob, Company: Acme\n` |
| `Ann Globex` | `Name: Ann, Company: Globex\n` |

## Автотесты

```bash
bash run_tests7_5.sh
```
