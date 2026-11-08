# GO_08_02. Идиома comma-ok — Тесты

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
| `3\ncat 5\ndog 7\nfish 2\ndog` | `7\n` |
| `1\na 0\na` | `0\n` |
| `1\na 1\nb` | `NOT FOUND\n` |
| `2\nx -1\ny 4\ny` | `4\n` |

## Автотесты

```bash
bash run_tests8_2.sh
```
