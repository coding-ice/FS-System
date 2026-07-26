# 仓库指南

## 项目结构与模块组织

这是一个使用 VitePress 构建的技术博客，所有发布内容均位于 `docs/`：

- `docs/frontend/`：前端笔记、示例和图片，按 `js/`、`css/`、`next/`、`write/` 等主题分类。
- `docs/backend/`：后端内容，目前包括 Python 和 Docker。
- `docs/.vitepress/config.mts`：站点信息、导航、侧边栏和 Markdown 扩展配置。
- `docs/public/`：全站静态资源；主题专属图片优先放在对应 Markdown 页面附近。

目录首页使用 `index.md`。可运行示例应与文章同目录，放入 `code/`、`demo/` 或 `components/`，例如 `docs/frontend/write/debounce/code/debounce.js`。

## 构建、测试与本地开发

使用 pnpm（仓库通过 `pnpm-lock.yaml` 锁定依赖）：

```bash
pnpm install       # 安装依赖
pnpm docs:dev      # 本地启动 VitePress
pnpm docs:build    # 构建生产站点到 docs/.vitepress/dist
pnpm docs:preview  # 本地预览构建产物
```

仓库未配置自动化测试、Lint 或格式化命令；`pnpm test` 会刻意报错，不能作为校验步骤。提交文档或配置改动前，运行 `pnpm docs:build`，并通过 `pnpm docs:dev` 手动检查受影响页面。

## 编码风格与命名

遵循相邻文件的既有风格：TypeScript/Vue 使用两空格缩进、双引号、分号和 `camelCase` 标识符；组件使用 PascalCase，例如 `Align.vue`。示例文件应使用清晰、贴合用途的名称。Markdown 标题层级要连贯，代码围栏必须指定语言。不要编辑生成目录 `.vitepress/cache`、`.vitepress/.temp` 或 `.vitepress/dist`。

## 技术内容与导航

新增需被读者发现的页面时，在 `docs/.vitepress/config.mts` 的对应侧边栏增加路由。VitePress 路由直接映射 `docs/` 路径：`docs/frontend/js/topic.md` 对应 `/frontend/js/topic`。提交前确认链接、图片和示例均能正确渲染。

AI 撰写或修改博客时，技术事实、API 用法、版本差异和最佳实践必须参考官方文档、标准规范或其他可核验的一手技术资料；不得凭空补全、盲目猜测或把不确定信息写成事实。引用外部资料时应核对其版本和适用范围，必要时在文章中附上来源链接。

## 博客正文风格

- 正文只写读者需要的技术知识、示例和结论，不写文件迁移、写作过程或章节编排等维护说明。
- 避免“本节用于……”“这些示例已迁移到……，用于对照阅读”等 AI 式元叙述；改为直接说明代码行为、适用条件和结论。
