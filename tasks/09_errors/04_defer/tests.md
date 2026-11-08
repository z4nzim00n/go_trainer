# GO_09_04. Порядок defer — Тесты

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
| `hive` | `open hive\nwork\nclose\n` |
| `go` | `open go\nwork\nclose\n` |
| `x` | `open x\nwork\nclose\n` |

## Автотесты

```bash
bash run_tests9_4.sh
```
