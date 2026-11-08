# GO_08_03. Уникальные элементы — Тесты

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
| `6\n3 1 3 2 1 4` | `Unique: 4\n1 2 3 4\n` |
| `2\n5 5` | `Unique: 1\n5\n` |
| `1\n-1` | `Unique: 1\n-1\n` |
| `0` | `Unique: 0\n\n` |

## Автотесты

```bash
bash run_tests8_3.sh
```
