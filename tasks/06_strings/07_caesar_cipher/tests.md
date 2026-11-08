# GO_06_07. Шифр Цезаря — Тесты

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
| `3` + `Hello, World!` | `Khoor, Zruog!\n` |
| `1` + `abcXYZ` | `bcdYZA\n` |
| `0` + `No change` | `No change\n` |
| `26` + `abc` | `abc\n` |
| `-1` + `abc` | `zab\n` |

## Автотесты

```bash
bash run_tests6_7.sh
```
