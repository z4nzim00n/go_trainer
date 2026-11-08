# GO_12_01. Проверка на простое число — Тесты

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
| `17` | `Prime\n` |
| `9` | `Not prime\n` |
| `1` | `Not prime\n` |
| `2` | `Prime\n` |
| `-5` | `Not prime\n` |
| `97` | `Prime\n` |

## Автотесты

```bash
bash run_tests12_1.sh
```
