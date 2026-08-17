"use client";

import React, { useState } from "react";
import useControllableValue from "../hooks/useControllableStatus";

const Counter = () => {
  // const [value, setvalue] = useState(0);

  // const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
  //   console.log(e.target.value);
  // };

  const [value, setvalue] = useControllableValue({
    defaultValue: 0,
    value: 100,
    onChange: (v) => console.log(v),
  });

  return (
    <div>
      counter: {value}
      <button
        className="border p-2 rounded-md"
        onClick={() => setvalue(value + 1)}
      >
        +
      </button>
    </div>
  );
};

export default Counter;
