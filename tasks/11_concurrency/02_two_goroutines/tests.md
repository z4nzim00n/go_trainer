# GO_11_02. Две горутины — Тесты

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
| `3 4` | `Sum: 14\n` |
| `0 5` | `Sum: 10\n` |
| `-1 2` | `Sum: 2\n` |

## Автотесты

```bash
bash run_tests11_2.sh
```
