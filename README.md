# 📦 Templafy — Discord Server Cloning Bot

Templafy is a powerful Discord bot that lets you **copy**, **save**, and **paste** entire server templates using slash commands.

No database. No bloat. Just structured backups and server transfers, made easy.

---

## ✨ Features

- 🧷 `/copy name:` — Save your server’s structure as a template
- 🚀 `/paste name:` — Instantly recreate it in a new server
- 📁 `/templates` — View your saved templates
- 🗑️ `/deletetemplate name:` — Delete a saved template
- 🧠 Works with roles, channels, categories, and hierarchy
- 💾 Uses JSON files (no database required)
- 🧪 Supports quick testing with `GUILD_ID` sync

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/Templafy.git
cd Templafy
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Setup `.env`

Create a `.env` file using the provided `.env.example`:

```env
DISCORD_TOKEN=your-bot-token
APPLICATION_ID=your-bot-app-id
GUILD_ID=your-test-guild-id  # Optional for development
```

### 4. Run the Bot

```bash
python bot.py
```

---

## 🛠 Commands Overview

| Command           | Description                          |
|-------------------|--------------------------------------|
| `/copy name:`     | Saves the current server as a template |
| `/paste name:`    | Pastes the template in current server |
| `/templates`      | Lists your saved templates           |
| `/deletetemplate` | Deletes one of your templates        |

> Templates are user-specific. You can only view or paste your own.

---

## 📂 Project Structure

```
Templafy/
├── bot.py
├── cogs/
│   ├── copy.py
│   ├── paste.py
│   └── templates.py
├── utils/
│   └── template_utils.py
├── templates/
│   └── saved.json
├── .env.example
├── requirements.txt
└── README.md
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Credits

Made by [yourusername](https://github.com/yourusername). Contributions welcome.
