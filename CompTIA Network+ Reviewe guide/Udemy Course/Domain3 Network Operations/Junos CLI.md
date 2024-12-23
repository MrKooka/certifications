**Junos CLI (Command Line Interface)** — это командная строка операционной системы **Junos**, которая используется для настройки, управления и мониторинга сетевого оборудования компании **Juniper Networks**. CLI является основным интерфейсом взаимодействия с устройствами Juniper (такими как маршрутизаторы, коммутаторы и брандмауэры), и предоставляет пользователям доступ к различным функциям и конфигурационным параметрам устройства.

### Основные особенности и функции Junos CLI:

1. **Уровни доступа**:
   - **Operational Mode (Операционный режим)**: используется для выполнения команд мониторинга и диагностики, просмотра состояния системы и интерфейсов, а также запуска утилит, таких как `ping` или `traceroute`.
   - **Configuration Mode (Режим конфигурации)**: предназначен для изменения конфигурации устройства. В этом режиме можно добавлять, изменять и удалять параметры конфигурации, такие как интерфейсы, маршруты, политики безопасности и т. д.

2. **Структурированная и иерархическая конфигурация**:
   - Конфигурация в Junos имеет иерархическую структуру, которая похожа на дерево. Это позволяет легко находить и изменять конкретные настройки устройства, что делает работу с CLI более логичной и организованной.
   - Используются команды `edit`, `set`, `delete` и `show` для навигации и изменения конфигурации на различных уровнях.

3. **Контекстно-зависимые команды**:
   - В Junos CLI команды зависят от контекста и текущего уровня конфигурации, на котором вы работаете. Например, если вы редактируете интерфейсы, команды будут касаться настройки и управления интерфейсами.

4. **Интерфейс автодополнения и помощи**:
   - Junos CLI поддерживает автодополнение команд и аргументов, что помогает ускорить ввод команд и снизить вероятность ошибок.
   - Команда `?` позволяет получить справку по доступным командам и их аргументам в текущем контексте.

5. **Операции с конфигурацией**:
   - **Кандидатная конфигурация**: В Junos все изменения сначала вносятся в так называемую "кандидатную" конфигурацию (candidate configuration), которая не влияет на работу устройства до тех пор, пока изменения не будут сохранены командой `commit`.
   - **Отмена изменений**: Можно легко откатить изменения до предыдущей версии конфигурации с помощью команды `rollback`.

6. **Диагностика и мониторинг**:
   - В операционном режиме доступны команды для диагностики состояния устройства (`show interfaces`, `show system uptime`, и т.д.).
   - Можно просматривать лог-файлы, проверять состояние сетевых интерфейсов, протоколов и

подключений с помощью команд `show`, что помогает в мониторинге и устранении неполадок.

### Примеры основных команд Junos CLI:

- **Переход в режим конфигурации**:
  ```
  configure
  ```
- **Просмотр текущей конфигурации**:
  ```
  show configuration
  ```
- **Настройка интерфейса**:
  ```
  set interfaces ge-0/0/0 unit 0 family inet address 192.168.1.1/24
  ```
- **Сохранение изменений**:
  ```
  commit
  ```
- **Откат изменений до предыдущей версии конфигурации**:
  ```
  rollback 1
  ```
- **Просмотр состояния интерфейсов**:
  ```
  show interfaces terse
  ```
- **Диагностика соединения**:
  ```
  ping 8.8.8.8
  ```
- **Проверка маршрутизации**:
  ```
  show route
  ```

### Заключение
Junos CLI — это мощный и гибкий инструмент для управления устройствами Juniper Networks. Его иерархическая структура и возможность автодополнения делают конфигурацию и диагностику сетевого оборудования интуитивно понятной и удобной, особенно для опытных сетевых инженеров.