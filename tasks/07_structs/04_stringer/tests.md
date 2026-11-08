# GO_07_04. Интерфейс Stringer — Тесты

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
| `21.5` | `Temp: 21.50°C\n` |
| `-5` | `Temp: -5.00°C\n` |
| `0` | `Temp: 0.00°C\n` |

## Автотесты

```bash
bash run_tests7_4.sh
```
