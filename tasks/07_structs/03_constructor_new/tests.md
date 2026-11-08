# GO_07_03. Конструктор NewUser — Тесты

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
| `Alice 30` | `Name: Alice, Age: 30\n` |
| `Bob 18` | `Name: Bob, Age: 18\n` |
| `Eve 0` | `Name: Eve, Age: 0\n` |

## Автотесты

```bash
bash run_tests7_3.sh
```
