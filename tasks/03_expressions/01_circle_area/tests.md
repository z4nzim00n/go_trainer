# GO_03_01. Площадь круга — Тесты

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
| `1` | `Area: 3.14\n` |
| `2` | `Area: 12.57\n` |
| `0` | `Area: 0.00\n` |
| `2.5` | `Area: 19.63\n` |

## Автотесты

```bash
bash run_tests3_1.sh
```
