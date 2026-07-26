import { defineConfig } from "vitepress";
import container from "markdown-it-container";
import { renderSandbox } from "vitepress-plugin-sandpack";
import { withMermaid } from "vitepress-plugin-mermaid";

// https://vitepress.dev/reference/site-config
export default withMermaid(defineConfig({
  title: "Full Stack Blog",
  description: "记录前端与后端开发实践的技术博客",
  markdown: {
    config(md) {
      md.use(container, "sandbox", {
        render(tokens, idx) {
          return renderSandbox(tokens, idx, "sandbox");
        },
      });
    },
  },
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: "前端", link: "/frontend/", activeMatch: "^/frontend(?:/|$)" },
      { text: "后端", link: "/backend/", activeMatch: "^/backend(?:/|$)" },
    ],

    sidebar: {
      "/frontend/": [
        {
          text: "前端",
          items: [{ text: "分类概览", link: "/frontend/" }],
        },
        {
          text: "HTML 与 CSS",
          items: [{ text: "Flex 布局", link: "/frontend/css/flex/" }],
        },
        {
          text: "JavaScript",
          collapsed: false,
          items: [
            { text: "概览", link: "/frontend/js/" },
            { text: "数据类型", link: "/frontend/js/data-types" },
            { text: "DOM 与事件", link: "/frontend/js/dom-event/" },
            { text: "BOM", link: "/frontend/js/bom/" },
            { text: "this", link: "/frontend/js/this" },
            { text: "运行原理与作用域", link: "/frontend/js/run-scope-chain/" },
            { text: "内存与闭包", link: "/frontend/js/memory-closure/" },
            { text: "浏览器渲染原理", link: "/frontend/js/populating/" },
            { text: "类与继承", link: "/frontend/js/class-extends/" },
            { text: "客户端存储", link: "/frontend/js/client-storage/" },
            { text: "Proxy 与 Reflect", link: "/frontend/js/es6/proxy-reflect/" },
            { text: "Iterator 与 Generator", link: "/frontend/js/es6/iterator-generator/" },
            { text: "Promise", link: "/frontend/js/es6/promise" },
          ],
        },
        {
          text: "Next.js",
          collapsed: false,
          items: [
            { text: "App Router", link: "/frontend/next/app-router" },
            { text: "动态、平行与拦截路由", link: "/frontend/next/routes-dynamic-group-parallel-intercept" },
            { text: "CSR / SSR / SSG / ISR", link: "/frontend/next/csr_ssr_ssg_isr" },
            { text: "渲染策略", link: "/frontend/next/rendering-strategy" },
            { text: "缓存", link: "/frontend/next/caching" },
            { text: "Server Actions", link: "/frontend/next/server-actions" },
          ],
        },
        {
          text: "其他主题",
          items: [
            { text: "Web3：EIP-6963", link: "/frontend/web3/eth/EIP6963" },
            { text: "算法与数据结构", link: "/frontend/algorithm/" },
          ],
        },
        {
          text: "JavaScript 实现",
          collapsed: true,
          items: [
            { text: "apply、call、bind", link: "/frontend/write/apply-call-bind/" },
            { text: "防抖", link: "/frontend/write/debounce/" },
            { text: "节流", link: "/frontend/write/throttle/" },
            { text: "深浅拷贝", link: "/frontend/write/deep-shallow-clone/" },
            { text: "new", link: "/frontend/write/new/" },
            { text: "instanceof", link: "/frontend/write/instanceof/" },
            { text: "Promise/A+", link: "/frontend/write/async/promise-a/" },
            { text: "场景实战", link: "/frontend/write/scene" },
          ],
        },
        {
          text: "前端面试",
          collapsed: true,
          items: [
            { text: "HTML 与 CSS", link: "/frontend/interview/html-css/" },
            { text: "JavaScript", link: "/frontend/interview/js/" },
            { text: "Web 安全", link: "/frontend/interview/security/" },
            { text: "网页关键指标", link: "/frontend/interview/web-vitals/" },
            { text: "缓存", link: "/frontend/interview/cache/" },
          ],
        },
      ],

      "/backend/": [
        {
          text: "后端",
          items: [{ text: "分类概览", link: "/backend/" }],
        },
        {
          text: "Python",
          collapsed: false,
          items: [
            { text: "概览", link: "/backend/python/" },
            { text: "迭代器与生成器", link: "/backend/python/iterator-generator/" },
          ],
        },
        {
          text: "Docker",
          collapsed: false,
          items: [
            { text: "概览", link: "/backend/docker/" },
            { text: "常用命令", link: "/backend/docker/basic/commands" },
          ],
        },
      ],
    },

    outline: {
      // 将页面的 H1 也纳入右侧目录；H2 及更低层级会按标题关系自动缩进。
      level: [1, 5],
    },

    lastUpdated: {
      text: "Last Updated",
    },
  },
}));
