import { Suspense } from "react";

export default async function Blog(props: PageProps<"/blog/[id]">) {
  return (
    <div>
      <h1>Blog</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <BlogContent {...props} />
      </Suspense>
      <div>footer</div>
    </div>
  );
}

async function BlogContent(props: PageProps<"/blog/[id]">) {
  const { id } = await props.params;
  // 模拟未缓存的请求时数据，约 3 秒后才能渲染
  await new Promise((resolve) => setTimeout(resolve, 3000));
  return <span>id: {id}</span>;
}
