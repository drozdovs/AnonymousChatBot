<div align="center">
  <h1>💬 Бот для анонимного общения</h1>
  <p>Анонимный чат в Telegram</p>

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-17-blue?logo=postgresql)
![Docker](https://img.shields.io/badge/Docker-compose-blue?logo=docker)
![Telegram](https://img.shields.io/badge/Telegram-bot-blue?logo=telegram)

</div>

## ✨ Возможности (Features)

- 💬 Анонимный чат
- 📱 Удобный интерфейс
- 🔍 Режимы поиска собеседника (M/Ж/+18)
- 👨‍💼 Панель администратора
- 👮‍♀️ Модерация
- 📨 Рассылка сообщений
- 🤝 Реферальная система
- 🏠 Создания анонимного групповых комнат
- 👥 Возможность добавлять собеседников в друзья
- 📊 Настройка рекламы
- 🐳 Легкое развертывание через **Docker**
- 🛡️ Безопасное хранение данных в **PostgreSQL**

## 💳 Платежи

Интеграция выполнена через [YooKassa](https://yookassa.ru). Оплаты проводятся с перенаправлением пользователя на страницу YooKassa.

## 🚀 Быстрый старт (Quickstart)

### Предварительные условия (Requirements)

- Docker и Docker Compose должны быть установлены
- Токен бота ([BotFather](https://t.me/botfather))

### Установка (Installation)

1. Клонируйте репозиторий

   ```bash
   git clone https://github.com/goldpulpy/AnonymousChatBot.git
   cd AnonymousChatBot
   ```

2. Скопируйте `.env.example` в `.env`:
   ```bash
   cp .env.example .env
   ```
3. Настройте переменные окружения:

   ```bash
    # Настройки бота (Telegram)
    BOT_TOKEN=YOUR_BOT_TOKEN # Токен бота из BotFather
    BOT_TIMEZONE=Europe/Moscow # Часовой пояс (Europe/Moscow)
    BOT_ADMINS=[00000000] # ID админов через запятую если несколько, Пример: [000,000]
    BOT_MODERS=[00000000] # ID Принимают жалобы через запятую
    BOT_USE_REDIS=False # Использовать Redis (По умолчанию False)

    # Настройки Базы данных (PostgreSQL)
    DB_HOST=db # Если вы запускаете через docker-compose.yml, то оставьте без изменений
    DB_PORT=5432 # Если вы запускаете через docker-compose.yml, то оставьте без изменений
    DB_NAME=YOUR_DB_NAME # Название БД, Например anonchat
    DB_USER=YOUR_DB_USER # Пользователь, Например root
    DB_PASSWORD=YOUR_DB_PASSWORD # Пароль, Например toor

    # Настройки Redis (Если не используете Redis, то оставьте без изменений)
    REDIS_HOST=redis
    REDIS_DB=13

    # Настройки платежей (YooKassa)
    PAYMENTS_SHOP_ID=YOUR_SHOP_ID # Идентификатор магазина
    PAYMENTS_SECRET_KEY=YOUR_SECRET_KEY # Секретный ключ
    PAYMENTS_RETURN_URL=https://example.com/return # URL возврата после оплаты
    PAYMENTS_ENABLED=False # Установите в True на production
   ```

`PAYMENTS_ENABLED=False` - Тестовый режим (имитация оплаты)

### Настройка цен (Setting prices)

Откройте файл `prices.py` и измените цены на нужные

### 📦 Развертывание (Deployment)

**Запустить бота:**

```bash
docker compose up -d
```

**Остановить бота:**

```bash
docker compose down
```
