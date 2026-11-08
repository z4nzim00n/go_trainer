# GO_03_02. Радианы в градусы — Тесты

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
| `3.141592653589793` | `Degrees: 180.00\n` |
| `1.5707963267948966` | `Degrees: 90.00\n` |
| `0` | `Degrees: 0.00\n` |
| `1` | `Degrees: 57.30\n` |

## Автотесты

```bash
bash run_tests3_2.sh
```
