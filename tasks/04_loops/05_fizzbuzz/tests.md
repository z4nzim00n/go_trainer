# GO_04_05. FizzBuzz — Тесты

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
| `5` | `1\n2\nFizz\n4\nBuzz\n` |
| `3` | `1\n2\nFizz\n` |
| `0` | *(пусто)* |
| `15` | `1\n2\nFizz\n4\nBuzz\nFizz\n7\n8\nFizz\nBuzz\n11\nFizz\n13\n14\nFizzBuzz\n` |

## Автотесты

```bash
bash run_tests4_5.sh
```
