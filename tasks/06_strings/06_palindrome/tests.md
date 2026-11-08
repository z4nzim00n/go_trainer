# GO_06_06. Палиндром — Тесты

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
| `A man, a plan, a canal: Panama` | `true\n` |
| `hello` | `false\n` |
| `12321` | `true\n` |
| *(пустая строка)* | `true\n` |
| `No lemon, no melon` | `true\n` |
| `abc` | `false\n` |

## Автотесты

```bash
bash run_tests6_6.sh
```
