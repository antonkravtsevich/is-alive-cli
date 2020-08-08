# is-alive-cli

Дай другим знать о состоянии своего интернет-соединения!

Бесплатно! Анонимно! Без рекламы! Без регистрации! Без хранения пресональных данных!

## Зачем?

Итак, предположим, что вскоре у тебя появяться проблемы с соединением, и какое-то время ты не сможешь выходить на связь. В то же время есть люди, которые были бы рады узнать, доступен ли ты сейчас или нет. 

Разумеется, ты хотел бы как-то сообщить им, что у тебя пробемы с соединением. Но как это сделать без самого соединения?

Для этой дилеммы есть решение - дай им знать твой текущий, постоянно обновляемый статус! Люди, которые на тебя полагаются, всегда будут знать, есть ли у тебя реальные проблемы с интернетом, или ты их просто игнорируешь.

## Как?

С помощью распределенной системы отчетности!

Работает это очень просто. В основе системы лежит [сервис](https://is-alive-21218.herokuapp.com/), принимающий постоянные обновления статуса с клиентских устройств. Как только обновления перестают поступать - сервис начинает обратный отсчет, и, если от тебя не поступит дальнейшей информации в течении фиксированного периода времени (на данный момент - 20 минут) - сервис начнет считать, что твое соединение отключилось. И даст знать об этом всем, с кем ты поделился персональной ссылкой.

## Вау, так круто, как мне подключится?

Рад, что ты заинтересовался. Подключится можно проще простого.

Первое, что тебе понадобится - это установить [Python](https://www.python.org/). Если на данном шаге тебе хочется закрыть страницу - можешь смело переходить к части [Easy mode](#easy-mode).

После установки python тебе понадобится установить зависимости:

```shell
pip install -r requirements.txt
```

После этого ты можешь смело запускать скрипт и подключаться к сервису!

```shell
python script.py
```

После запуска скрипт выдаст тебе твою пресональную ссылку - делись ей со всеми, чья осведомленность о твоем доступе к интернету кажется тебе важной. 


## F.A.Q. по скрипту (на самом деле эти вопросы никто не задавал, но, возможно, тебе будет интересно)

### Как работает скрипт?

Принцип работы скрпта крайне прост. При первом запуске скрипт генерирует **твой уникальный идентификатор** - строку вида `aec2cbfc-d8f6-11ea-b55f-48a472a00c26`. Эта строка сохраняется в конфигурационном файле conf.json и используется при генерации запросов к сервису. Запрос для обновления статуса, собственно, содержит только твой идентификатор - этих данных сервису достаточно, чтобы поддерживать информацию о состоянии твоего соединения актуальной. Запросы отправляются раз в минуту. 

### То есть что, мне надо все время держать скрипт запущенным, чтобы сервис поддерживал мой статус обновленным?

Да.

### Разве нету более... изящных способов реализации такой задачи?

Возможно.

### Что делать, если я хочу завершить работу скрипта, но при этом не хочу иметь оффлайн-статус?

Смело нажимай Ctrl+C в терминале\консоли, где запущен процесс. Перед отключением скрипт автоматически зарегистрирует ручное выключение, отправив запрос на дополнительный адрес, и в твоем статусе будет значится гордое "Соединение было отключено пользователем".

### Могу ли я перезапустить скрипт так, чтобы предыдущая персональная ссылка осталась активной?

Несомненно. Твой уникальный ID, как уже было сказано выше, сохраняется в конфигурационном файле. Если конфигурационный файл существует - при перезапуске скрипт будет использовать ID из файла вместо создания нового.

### Почему дизайн выглядит так, как будто его писал разработчик из 90-х с цветовой слепотой?

В основном потому, что я не фронт-энд разработчик. А еще потому, что работу он свою выполняет и так, а в конкурсе юзабилити этому сервису все равно никогда не участвовать.

### У меня есть крутая идея для дополнения сервиса. Могу ли я добавить новую фичу?

Разумеется. Я буду рад глянуть любые merge-реквесты, хоть и факт их появления кажется мне крайне маловероятным. 

### Могу ли я вносить изменения в код скрипта?

В теории можешь, но за последствия я не ручаюсь. 

## Easy mode

Не имеешь возможности устанавливать Python и запускать скрипты, но сведениями о стостоянии интернета все же хочешь поделиться? 

Что-ж, задача трудная, но решение для нее все же есть, хоть и не идеальное. Ты можешь поделиться ссылкой на [основную страницу сервера](https://is-alive-21218.herokuapp.com/). На ней расположен список уже подключенных клиентов.

Велика вероятность, что при возникновении массовых сбоев в сети большое количество клиентов будет иметь проблемы с подключением. Так что если в таблице все подряд имеют статус "Соединение отсутствует" - вполне можно предположить, что конкретно у тебя тоже будут проблемы с доступом. 

## Контакты

По вопросам внезапных падений можете писать в телеграмм - [@anton_kravtsevich](https://t.me/anton_kravtsevich). Я отвечу по первой возможности - если, разумеется, у меня будет доступ к интернету.