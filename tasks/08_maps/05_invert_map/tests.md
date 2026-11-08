# GO_08_05. Инверсия map — Тесты

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
| `3\na 1\nb 2\nc 3` | `1: a\n2: b\n3: c\n` |
| `2\nz 10\ny 5` | `5: y\n10: z\n` |
| `1\nsolo 42` | `42: solo\n` |

## Автотесты

```bash
bash run_tests8_5.sh
```
