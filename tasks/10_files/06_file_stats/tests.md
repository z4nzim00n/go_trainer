# GO_10_06. Статистика файла — Тесты

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
| `f.txt` (`a\nb\n`) | `Lines: 2\nBytes: 4\n` |
| `empty.txt` | `Lines: 0\nBytes: 0\n` |
| `f.txt` (`hello`) | `Lines: 1\nBytes: 5\n` |
| `f.txt` (`x\ny`) | `Lines: 2\nBytes: 3\n` |

## Автотесты

```bash
bash run_tests10_6.sh
```
