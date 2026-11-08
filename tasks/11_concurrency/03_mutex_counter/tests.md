# GO_11_03. Счётчик с Mutex — Тесты

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
| `4` | `Counter: 4000\n` |
| `1` | `Counter: 1000\n` |
| `0` | `Counter: 0\n` |
| `3` | `Counter: 3000\n` |

## Автотесты

```bash
bash run_tests11_3.sh
```
