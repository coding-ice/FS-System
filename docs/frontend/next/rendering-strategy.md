# 渲染策略

## 静态渲染 (Static Rendering)

在构建时，Next.js 会生成对应的产物，页面在构建时就被预渲染为静态 HTML。

### 特点：

- **构建时生成**：页面在 `next build` 时就被预渲染
- **缓存友好**：生成的静态文件可以被 CDN 缓存
- **性能优异**：用户访问时直接返回预生成的 HTML，无需服务器计算
- **SEO 友好**：搜索引擎可以直接抓取完整的 HTML 内容

### 使用场景：

- 博客文章
- 产品展示页面
- 文档页面
- 营销页面
- 任何内容相对固定的页面

### 实现方式：

```typescript
// 默认行为，无需特殊配置
export default function Page() {
  return <h1>静态页面</h1>;
}

// 或者显式指定
export const dynamic = "force-static";
```

## 动态渲染 (Dynamic Rendering)

**动态渲染策略和数据请求缓存是分开的, 有些规则可以动态渲染，同时退出数据缓存**

可以动态生成内容，每次请求时都会在服务器端重新渲染页面。

### 特点：

- **请求时生成**：页面在每次请求时动态渲染
- **实时数据**：可以获取最新的数据
- **个性化内容**：可以为不同用户生成不同的内容
- **服务器负载**：每次请求都需要服务器计算

### 使用场景：

- 用户仪表板
- 购物车页面
- 实时数据展示
- 需要用户认证的页面
- 个性化内容页面

### 实现方式：

```typescript
// 方式1：使用 dynamic 配置
export const dynamic = "force-dynamic";

// 方式2：使用动态函数
export default async function Page() {
  const data = await fetch("https://api.example.com/data", {
    cache: "no-store", // 禁用缓存
  });
  return <h1>动态内容: {data.title}</h1>;
}

// 方式3：使用 cookies() 或 headers()
import { cookies } from "next/headers";

export default function Page() {
  const cookieStore = cookies();
  return <h1>Cookie: {cookieStore.get("theme")?.value}</h1>;
}
```

## 主要区别对比

| 特性           | 静态渲染       | 动态渲染         |
| -------------- | -------------- | ---------------- |
| **生成时机**   | 构建时         | 请求时           |
| **性能**       | 极快（预生成） | 较慢（实时计算） |
| **缓存**       | 可缓存         | 不可缓存         |
| **数据新鲜度** | 构建时的数据   | 实时数据         |
| **服务器负载** | 无             | 高               |
| **SEO**        | 优秀           | 良好             |
| **个性化**     | 不支持         | 支持             |

## 混合使用

Next.js 支持在同一应用中混合使用静态和动态渲染：

```typescript
// 静态部分
export default function Page() {
  return (
    <div>
      <h1>静态标题</h1>
      <DynamicComponent />
    </div>
  );
}

// 动态组件
import dynamic from "next/dynamic";

const DynamicComponent = dynamic(() => import("./DynamicComponent"), {
  ssr: false, // 客户端渲染
});
```

## Streaming

Streaming / loading.js ，允许逐步渲染页面内容：

```typescript
// 使用 Suspense 实现流式渲染
import { Suspense } from "react";

export default function Page() {
  return (
    <div>
      <h1>立即显示</h1>
      <Suspense fallback={<p>加载中...</p>}>
        <SlowComponent />
      </Suspense>
    </div>
  );
}
```
