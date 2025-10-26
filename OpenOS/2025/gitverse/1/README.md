# Система аудита ОС

## Возможности
 - мониторинг модификаций файлов и прав доступа в указываемых директориях
 - сохранение отчетов о модификациях в git репозиторий
 - фильтрация мониторинга на основе black-list/white-list
 - трекинг отдельных файлов с полной историей изменений
 - формирование drift-check отчета о модификации в диапазоне истории репозитория
 - возможность интеграции в systemctl
 - возможность отката содержимого отдельных файлов
 - батчинг отчетов с заданной периодичностью
 - gpg подпись коммитов

Поддерживаемые команды:
 - `monitor`: запуск мониторинга в реальном времени
 - `snapshot`: создание snapshot коммита для упрещения трекинга истории репозитория
 - `drift-check`: создание отчета об отклонеии конфигурации
 - `roll-back`: откат содержимого файлов

## Зависимости

 - Python 3.7+
   - `gitpython` (`pip3 install GitPython`)
   - `pyinotify` (`pip3 install pyinotify`)
 - Git с настроенной подписью GPG

Установка зависимостей:
```bash
pip3 install GitPython pyinotify
```


## Поддерживаемые команды

### `monitor` - Мониторинг в реальном времени

Команда отслеживает изменения в директориях и автоматически фиксирует события
в git репозитории.

Каждое зафиксированное изменение коммитится в репозиторий в виде коммита в формате:
```
[{timestamp}]: {tracked?} file {created|deleted|modified|changed attributes to {attr}} by {process pid}
```
Коммит подписывается цифровой gpg подписью, указанной предварительно пользователем через
```bash
git config --global user.signingkey {key}
```

#### Параметры
```
sysaudit.py monitor [-h] [--help] --watch WATCH [--watch WATCH [...]] [--ignore IGNORE [...]] [--keep KEEP [...]] [--track TRACK [...]] --repo REPO [--squash-period SQUASH_PERIOD] [--log LOG]
```
| Флаг              | Описание |
|-------------------|----------|
| `--watch`         | Директории для мониторинга, можно указать несколько, можно относительные пути |
| `--ignore`        | Паттерны файлов, которые игнорируются при мониторинге (например, `*.tmp`, `*.sw?`), можно указать несколько |
| `--keep`          | Паттерны файлов, которые не игнорируются, даже если попадают под `--ignore`, можно указать несколько |
| `--track`         | Файлы, которые отслеживаются полностью - с возможностью отката, можно указать несколько, можно отностлельные пути |
| `--repo`          | Путь к Git-репозиторию для хранения аудит-логов, можно относительный путь |
| `--squash-period` | Интервал (в секундах) для объединения событий в пакеты (по умолчанию: 5) |
| `--log`           | Файл журнала или `stdout` (по умолчанию: `stdout`) |

#### Пример использования

```bash
python3 sysaudit.py monitor     \
  --watch /etc                  \
  --watch /var/log              \
  --ignore '*.tmp'              \
  --ignore '*.log'              \
  --ignore '.*'                 \
  --keep ".important"           \
  --track /etc/nginx/nginx.conf \
  --repo /path/to/audit-repo    \
  --squash-period 10            \
  --log audit.log
```

---

### `snapshot` - Создание снимка

Cоздание snapshot коммита с описанием.

#### Параметры
```
sysaudit.py snapshot [-h] [--help] --message MESSAGE --repo REPO
```

| Флаг              | Описание |
|-------------------|----------|
| `--message`       | Сообщение в создаваемом коммите |
| `--repo`          | Путь к Git-репозиторию |

#### Пример использования

```bash
python3 sysaudit.py snapshot                         \
  --message "===== BASELINE AFTER CONFIG SYNC =====" \
  --repo /path/to/audit-repo
```

---

### `drift-check` Отчет об отклонеии конфигурации

Сравнить список изменений конфигураций относительно оказанного коммита

#### Параметры
```
sysaudit.py drift-check [-h] [--help] --baseline BASELINE --repo REPO
```
| Флаг              | Описание |
|-------------------|----------|
| `--baseline`      | SHA коммита (в git формате) относительно которого формировать отчет |
| `--repo`          | Путь к Git-репозиторию |

#### Пример использования

```bash
python3 sysaudit.py drift-check \
  --baseline abc123def456 \
  --repo /path/to/audit-repo
```
```bash
python3 sysaudit.py drift-check \
  --baseline HEAD^^^ \
  --repo /path/to/audit-repo
```

---

### `rollback` - Откат изменений

Вернуть отслеживаемый файл к указанному состоянию. При этом так-же создается коммит в репозитории с описанием роллбека. Файл должен предварительно отслеживаться командой `monitor --track {file}` для возможности получения истории

#### Параметры

sysaudit.py rollback [-h] [--help] --path PATH [--path PATH [...]] --to-commit TO_COMMIT --repo REPO [--dry-run]

| Флаг              | Описание |
|-------------------|----------|
| `--path`          | Путь к файлу для отката, можно несколько, можно относительный путь) |
| `--to-commit`     | SHA коммита (в git формате) к которому возвратить состояние файла |
| `--repo`          | Путь к Git-репозиторию |
| `--dry-run`       | Только напечатать команды, не производить откат |

```bash
python3 sysaudit.py rollback    \
  --to-commit abc123def456      \
  --path /etc/nginx/nginx.conf  \
  --path ~/.ssh/known_hosts     \
  --repo /path/to/audit-repo
```

---

# Запуск в качестве systemctl сервиса

Чтобы запустить sysaudit в качестве sysaudit сервиса необходимо:

1. Создать пользователя и группу для запуска сервиса:
```bash
sudo useradd -m -s /bin/bash audit-user
sudo addgroup audit-group
sudo usermod -aG audit-group audit-user
```

2. Создать директорию для работы сервиса:
```bash
sudo mkdir -p /home/audit-user/
sudo chown audit-user:audit-user /home/audit-user/
```

3. Переместить скрипт в директорию сервиса:
```bash
sudo cp sysaudit.py /home/audit-user/
sudo chown audit-user:audit-user /home/audit-user/sysaudit.py
sudo chmod 750 /home/audit-user/sysaudit.py
```

4. Установить все python зависимости от имени пользователя `audit-user`,
   или же создать virtual-venv в директории со скриптом

5. Переместить файл `sysaudit.service` в `/etc/systemd/system/`:
```bash
sudo cp sysaudit.service /etc/systemd/system/sysaudit.service
```

6. Перезапустить systemctl и запустить сервис
```bash
sudo systemctl daemon-reload
sudo systemctl restart sysaudit.service
sudo systemctl status sysaudit.service
```
