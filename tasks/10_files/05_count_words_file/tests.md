# GO_10_05. Слова в файле — Тесты

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
| `text.txt` (`one two\nthree\n`) | `Words: 3\n` |
| `empty.txt` | `Words: 0\n` |
| `text.txt` (`a`) | `Words: 1\n` |

## Автотесты

```bash
bash run_tests10_5.sh
```
