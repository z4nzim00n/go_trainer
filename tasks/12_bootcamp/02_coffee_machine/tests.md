# GO_12_02. Кофейный автомат — Тесты

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
| `3\n20 20 20` | `Coffee: 10\n` |
| `1\n20` | `Need: 30\n` |
| `2\n50 10` | `Coffee: 10\n` |
| `0` | `Need: 50\n` |

## Автотесты

```bash
bash run_tests12_2.sh
```
