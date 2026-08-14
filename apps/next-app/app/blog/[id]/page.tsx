import React, { Suspense } from "react";

const Blog = async (props: PageProps<"/blog/[id]">) => {
  return (
    <div>
      <h1>Blog</h1>
      <Suspense fallback={<div>Loading...</div>}>
        <BlogContent {...props} />
      </Suspense>
      <div>footer</div>
    </div>
  );
};

export default Blog;

const BlogContent = async (props: PageProps<"/blog/[id]">) => {
  const { id } = await props.params;
  await new Promise((resolve) => setTimeout(resolve, 3000));
  return <span>id: {id}</span>;
};
