# GO_10_04. Сумма чисел из файла — Тесты

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
| `numbers.txt` (`1 2 3\n`) | `Sum: 6\n` |
| `empty.txt` | `Sum: 0\n` |
| `numbers.txt` (`10\n-5\n2`) | `Sum: 7\n` |

## Автотесты

```bash
bash run_tests10_4.sh
```
