# Server Actions

Server Actions 是在服务端执行的异步函数，可以在服务端组件和客户端组件中使用，处理 nextjs 应用中的数据和更改

## 模式

### 模块级别

```tsx
// app/actions.tsx
"use server";

const data = ["吃饭", "睡觉", "coding"];

async function getTodos() {
  return data;
}
```

- 可以在服务端/客户端组件使用

### 函数级别

```tsx
// app/page.tsx
export default function Page() {
  async function getTodos() {
    "use server";
    const data = ["吃饭", "睡觉", "coding"];
    return data;
  }
}
```

- 只能在服务端组件只使用

## 应用场景

- 在 page router 中采用传统接口调用模式时，需要先定义接口，再由客户端调用并完成数据交互
- 在 app router 中，这种操作可以直接简化为 server actions

### Page Router

```ts
// app/api/todo-list/route.ts
import { NextRequest, NextResponse } from "next/server";

const data = ["吃饭", "冥想", "打豆豆"];

export function GET() {
  return NextResponse.json({ data });
}

export async function POST(request: NextRequest) {
  const formData = await request.formData();
  const result = formData.get("key") as string;
  data.push(result);
  return NextResponse.json({ data });
}
```

```tsx
// pages/form.tsx

"use client";

import { FormEvent, useEffect, useState } from "react";

function Form() {
  const [todos, setTodos] = useState([]);

  useEffect(() => {
    async function getTodos() {
      const res = await fetch("/api/todo-list");
      const data = await res.json();
      setTodos(data.data);
    }
    getTodos();
  }, []);

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    const res = await fetch("/api/todo-list", {
      method: "POST",
      body: new FormData(e.target as HTMLFormElement),
    });
    const data = await res.json();
    setTodos(data.data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="text" name="key" />
        <button type="submit">Add</button>
      </form>
      <h3>Todo List</h3>
      <ul>
        {todos.map((todo) => (
          <li key={todo}>{todo}</li>
        ))}
      </ul>
    </div>
  );
}

export default Form;
```

### App Router

```tsx
// app/form/actions.ts
"use server";

import { revalidatePath } from "next/cache";

const data = ["吃饭", "睡觉", "coding"];

async function getTodos() {
  return data;
}

async function addTodos(formData) {
  const todo = formData.get("todo");
  data.push(todo);
  revalidatePath("/form");
  return data;
}
```

```tsx
// app/form/page.tsx
import { getTodos, addTodos } from "./actions";

async function Page() {
  const todos = await getTodos();

  return (
    <>
      <form action={addTodos}>
        <input name="todos" />
        <button type="submit">add</button>
      </form>
      <ul>
        {todos.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </>
  );
}

export default Page;
```

## 原理

当 form action 触发，实际是向当前页面发送了一个 post 请求，form 标签中注入了一个 hidden 的 input，带有一个 action_id 用于区分是哪个 form 的请求

```html
<form>
  <input
    type="hidden"
    name="$ACTION_ID_7f8a5a30e5f9c77460d0fb2c8e233829af998c237b"
  />
</form>
```

## 实战案例

```tsx
// actions.ts
"use server";

import { revalidatePath } from "next/cache";
const todos = ["吃饭", "睡觉", "coding"];

export async function getTodos() {
  return todos;
}

export async function createTodo(_, formData: FormData) {
  const todo = formData.get("todo") as string;
  await new Promise((resolve) => setTimeout(resolve, 1000));
  todos.push(todo);
  revalidatePath("/form-actions-3");
  return {
    message: `add ${todo} success`,
  };
}
```

```tsx
// form/form.tsx
"use client";

import { useActionState } from "react";
import { createTodo } from "./actions";

const FormActions = () => {
  const [state, formAction, isPending] = useActionState(createTodo, {
    message: "",
  });

  return (
    <form action={formAction}>
      <input type="text" name="todo" />
      <button type="submit">{isPending ? "Adding..." : "Add"}</button>
      <p>{state.message}</p>
    </form>
  );
};

export default FormActions3;
```

```tsx
import { getTodos } from "./actions";
import FormActions from "./form";

const FormActions3Page = async () => {
  const todos = await getTodos();

  return (
    <div>
      <FormActions />
      <ul>
        {todos.map((todo) => (
          <li key={todo}>{todo}</li>
        ))}
      </ul>
    </div>
  );
};

export default FormActions3Page;
```
