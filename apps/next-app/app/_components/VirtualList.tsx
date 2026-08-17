"use client";

import renderUserList from "@/mock/user-list";
import { getVirtualIdxs } from "@/util/getVirtualIdxs";
import React, { useState } from "react";

const userList = renderUserList();
const containerHeight = 500;
const itemHeight = 50;

const VirtualList = () => {
  const [scrollTop, setScrollTop] = useState(0);
  const { startIdx, endIdx } = getVirtualIdxs(
    containerHeight,
    itemHeight,
    userList.length,
    scrollTop,
  );

  return (
    <div
      style={{ height: containerHeight, overflowY: "auto", width: "400px" }}
      onScroll={(event) =>
        setScrollTop((event?.target as HTMLDivElement)?.scrollTop ?? 0)
      }
    >
      <div
        style={{ height: userList.length * itemHeight, position: "relative" }}
      >
        <ul style={{ transform: `translateY(${startIdx * itemHeight}px)` }}>
          {userList.slice(startIdx, endIdx).map((user) => (
            <li
              key={user.id}
              style={{ height: itemHeight, borderBottom: "1px solid #000" }}
            >
              {user.name}
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default VirtualList;
