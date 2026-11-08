# Разбор задания

## Горутина

~~~go
go func() {
    fmt.Println("worker")
}()
~~~

`go` запускает функцию параллельно. Главная горутина при этом продолжает
работу и может завершиться раньше — тогда программа закончится.

## Канал для ожидания

~~~go
start := make(chan struct{})
done := make(chan struct{})
go func() {
    <-start
    fmt.Println("worker")
    close(done)
}()
fmt.Println("main")
close(start)
<-done
fmt.Println("finished")
~~~

`struct{}` — пустой тип, он ничего не занимает. Такой канал используют только
как сигнал.

## Гонка

Без синхронизации порядок вывода `main` и `worker` не определён. Канал
делает порядок предсказуемым.
