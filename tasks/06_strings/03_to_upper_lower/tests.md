# GO_06_03. Верхний и нижний регистр — Тесты

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
| `hello` + `WORLD` | `HELLO\nworld\n` |
| `Go` + `Lang` | `GO\nlang\n` |
| *(две пустые строки)* | `\n\n` |

## Автотесты

```bash
bash run_tests6_3.sh
```
