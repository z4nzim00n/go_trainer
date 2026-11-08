# GO_06_04. Количество слов — Тесты

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
| `hello world` | `2\n` |
| *(пустая строка)* | `0\n` |
| `  a  b   c ` | `3\n` |
| `one` | `1\n` |
| `a\tb\nc` | `3\n` |

## Автотесты

```bash
bash run_tests6_4.sh
```
