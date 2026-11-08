# GO_06_05. Разворот строки — Тесты

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
| `hello` | `olleh\n` |
| `Go` | `oG\n` |
| *(пустая строка)* | `\n` |
| `abc def` | `fed cba\n` |

## Автотесты

```bash
bash run_tests6_5.sh
```
