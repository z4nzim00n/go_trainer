# GO_10_01. Чтение файла — Тесты

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
| `f1.txt` (`hello\nworld\n`) | `hello\nworld\n` |
| `f1.txt` (`abc`) | `abc` |
| `missing.txt` | `Error: cannot read file\n` |

## Автотесты

```bash
bash run_tests10_1.sh
```
