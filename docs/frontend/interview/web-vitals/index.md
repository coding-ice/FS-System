# 网页核心指标

## DCL L

### DCL

- 指的是 (DOMContentLoaded) dom 树解析完毕，与任何外部加载的资源无关

### L

- load 外部资源加载完毕的时间点

<<< ./code/dcl_l.html

## FP FCP

### FP (first paint)

- 浏览器首次绘制任何内容到屏幕上的时间点（白屏时间，可能看不见）

### FCP (first contentful paint)

- 浏览器首次绘制任何有意义内容到屏幕上的时间点 （用户能看到的第一个内容）

<<< ./code/fp_fcp.html

## LCP

- 最大内容绘制时间点 (largest contentful paint)
- 页面主要内容加载完成的时间点
- <= 2.5s 优秀 | <= 4.0s 需要改进 | > 4.0s 差

## TTFB
- 首字节时间 (time to first byte)
- 浏览器发送请求到接收到响应的第一个字节的时间
- 一般在 SSR 场景下比较重要
- <= 200ms 优秀 | <= 600ms 需要改进 | > 600ms 差
