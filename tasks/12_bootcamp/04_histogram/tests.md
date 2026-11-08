# GO_12_04. Гистограмма — Тесты

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
| `5\n1 2 1 3 3` | `1: **\n2: *\n3: **\n` |
| `3\n9 9 9` | `9: ***\n` |
| `0` | *(пусто)* |

## Автотесты

```bash
bash run_tests12_4.sh
```
