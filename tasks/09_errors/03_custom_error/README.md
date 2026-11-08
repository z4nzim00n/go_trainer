## GO_09_03. Своя ошибка

### Задание
| GO_09_03 ||
| ------ | ------- |
| **Темы:** | тип-ошибка, `Error()`, `errors.As` |
| **Файл решения:** | main.go |
| **Входные данные:** | Возраст одним числом |
| **Выходные данные** | Стандартный поток вывода (stdout) |


Объяви тип `ValidationError` с полем `Field` и методом `Error() string`.
Функция `ValidateAge(age int) error` возвращает `&ValidationError{Field: "age"}`,
если возраст отрицательный. Выведи `Age: ...` или `Validation error: age`.

~~~text
Validation error: age
~~~

### Примеры

| Входные данные | Результат работы |
| ------ | ------ |
| -1 | Validation error: age |
| 20 | Age: 20 |

### Как проверить

```bash
bash run_tests9_3.sh
```
