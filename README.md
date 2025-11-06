# TarTab

Tab Your Mind — 打开标签页，点亮你的思维

一个集成了 Web 前端、Chrome 扩展和 FastAPI 后端的 AI 资源与灵感启动页项目。

## 项目结构

```
tartab/
├── web/          # Vue3 + Vite 前端
├── extension/    # Chrome 扩展
└── backend/      # FastAPI 后端
```

## 快速开始

### Web 前端

```bash
cd tartab/web
npm install
npm run dev
```

### Chrome 扩展

1. 打开 Chrome 浏览器
2. 访问 `chrome://extensions/`
3. 开启"开发者模式"
4. 点击"加载已解压的扩展程序"
5. 选择 `tartab/extension` 目录

### FastAPI 后端

```bash
cd tartab/backend
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

## 功能特性

- 🎨 现代化的深色主题 UI (Tailwind CSS)
- 📱 响应式设计
- ⚡ Vue3 + Vite 快速开发
- 🔌 Chrome 新标签页覆盖
- 🚀 FastAPI 后端 API

## 开发

项目使用 Vue3、Tailwind CSS 和 FastAPI 构建，支持快速开发和部署。

