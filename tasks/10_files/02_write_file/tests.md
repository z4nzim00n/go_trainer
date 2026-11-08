# GO_10_02. Запись файла — Тесты

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
| `out.txt hello` | `Saved: hello\n` |
| `out.txt Go` | `Saved: Go\n` |

## Автотесты

```bash
bash run_tests10_2.sh
```
