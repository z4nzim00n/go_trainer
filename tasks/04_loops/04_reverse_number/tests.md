# GO_04_04. Разворот числа — Тесты

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
| `12340` | `4321\n` |
| `0` | `0\n` |
| `100` | `1\n` |
| `7` | `7\n` |
| `1234567899` | `9987654321\n` |
| `-123` | `321\n` |

## Автотесты

```bash
bash run_tests4_4.sh
```
