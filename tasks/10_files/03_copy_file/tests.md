# GO_10_03. Копирование файла — Тесты

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
| `f1.txt f2.txt` (`hello\n`) | `Copied: hello\n` |
| `f1.txt f2.txt` (`a b\n`) | `Copied: a b\n` |
| `missing.txt f2.txt` | `Error: cannot read source\n` |

## Автотесты

```bash
bash run_tests10_3.sh
```
