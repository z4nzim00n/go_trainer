# Разбор задания

## Пул воркеров

~~~go
jobs := make(chan int)
results := make(chan int)
var wg sync.WaitGroup

for i := 0; i < 3; i++ {
    wg.Add(1)
    go func() {
        defer wg.Done()
        for j := range jobs {
            results <- j * j
        }
    }()
}
~~~

Все воркеры читают из одного канала `jobs` — работа распределяется
автоматически.

## Завершение

~~~go
go func() {
    for i := 1; i <= n; i++ {
        jobs <- i
    }
    close(jobs)
    wg.Wait()
    close(results)
}()
~~~

Сначала закрываем `jobs`, затем ждём воркеров, и только потом закрываем
`results`. Если закрыть `results` раньше, воркеры запаникуют.

## Почему пул

Создавать горутину на каждую задачу накладно. Пул ограничивает число
одновременных работников.
