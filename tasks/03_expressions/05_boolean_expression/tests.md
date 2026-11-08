# GO_03_05. Логическое выражение — Тесты

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
| `9` | `true\n` |
| `17` | `true\n` |
| `10` | `false\n` |
| `21` | `true\n` |
| `0` | `true\n` |
| `7` | `true\n` |

## Автотесты

```bash
bash run_tests3_5.sh
```
