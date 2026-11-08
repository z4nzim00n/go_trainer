# GO_08_04. Группировка по длине — Тесты

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
| `a cat dog bee` | `1: a\n3: bee cat dog\n` |
| `go` | `2: go\n` |
| `dd cc a bbb` | `1: a\n2: cc dd\n3: bbb\n` |

## Автотесты

```bash
bash run_tests8_4.sh
```
