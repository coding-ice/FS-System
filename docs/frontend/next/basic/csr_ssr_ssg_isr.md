# 客户端 / 服务端 / 静态站点生成 / 增量静态再生

## CSR

只返回一个很小的 html （div#root），渲染工作在客户端完成

## SSR

渲染工作在服务端完成，请求数据必须在渲染之前  
它是线性的

请求数据 -> 返回静态的 HTML 给客户端 -> 不可交互 -> 水合 -> 可交互的应用

```tsx
const Page = ({ data }) => {
  return <div>{JSON.stringify(data)}</div>;
};

// 每次请求的时候执行
export async function getServerSideProps() {
  const res = await fetch("https://jsonplaceholder.typicode.com/todos");
  const data = await res.json();

  return {
    props: { data },
  };
}

export default Page;
```

## SSG 静态站点生成

对于那种纯静态的页面，直接提前生成 HTML 文件即可，访问也最快

## ISG

纯静态页面中，比如博客（点赞/评论等）这些数据又要是动态的，所有就有了增量静态再生，设置一个重新验证的时间

```tsx
const Page = ({ post, num }) => {
  return (
    <>
      <p>{post.title}</p>
      <p>{post.body}</p>
      <p>count: {num}</p>
    </>
  );
};

export default Page;

// 获取多个路径
export const getStaticPaths = async () => {
  const res = await fetch("https://jsonplaceholder.typicode.com/posts");
  const posts = await res.json();

  return {
    paths: posts.slice(0, 5).map((post) => {
      return {
        params: {
          id: post.id.toString(),
        },
      };
    }),
    fallback: "blocking",
  };
};

const getNumber = (num: number) => Math.floor(Math.random() * num);

// 获取单个路径
export const getStaticProps = async ({ params }) => {
  const res = await fetch(
    `https://jsonplaceholder.typicode.com/posts/${params.id}`
  );
  const post = await res.json();

  return {
    props: { post, num: getNumber(100) },
    revalidate: 10,
  };
};

```
