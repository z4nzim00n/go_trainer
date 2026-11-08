# GO_08_01. Подсчёт слов через map — Тесты

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
| `apple banana apple` | `apple: 2\nbanana: 1\n` |
| `a` | `a: 1\n` |
| `b a b a b` | `a: 2\nb: 3\n` |

## Автотесты

```bash
bash run_tests8_1.sh
```
