## GO_09_05. panic и recover

### Задание
| GO_09_05 ||
| ------ | ------- |
| **Темы:** | `panic`, `recover`, отложенная функция |
| **Файл решения:** | main.go |
| **Входные данные:** | Два целых числа A и B |
| **Выходные данные** | Стандартный поток вывода (stdout) |


Напиши `SafeDivide(a, b int) (int, error)`. При `b == 0` вызови
`panic("division by zero")`, перехвати панику через `recover` в `defer`
и верни её как ошибку. Выведи `Result: ...` или `Recovered: division by zero`.

~~~text
Recovered: division by zero
~~~

### Примеры

| Входные данные | Результат работы |
| ------ | ------ |
| 10 2 | Result: 5 |
| 5 0 | Recovered: division by zero |

### Как проверить

```bash
bash run_tests9_5.sh
```
