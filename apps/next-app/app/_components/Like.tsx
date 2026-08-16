"use client";

import { useState } from "react";
import dynamic from "next/dynamic";

const Like = () => {
  const [count, setCount] = useState(0);
  console.log("预渲染构建了");

  return (
    <button type="button" onClick={() => setCount((n) => n + 1)}>
      Like {count}
    </button>
  );
};

export default Like;
// export default dynamic(() => Promise.resolve(Like), {
//   ssr: false,
//   loading: () => <div>Loading...</div>,
// });
