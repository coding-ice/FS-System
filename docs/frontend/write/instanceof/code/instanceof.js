function MyInstanceof(a, b) {
  // 1. 如果是 null 或者 非对象及函数类型 -> 直接返回 false
  if (a === null || (typeof a !== "object" && typeof a !== "function")) {
    return false;
  }

  // 2. 先获取 a 的隐式原型
  let proto = Object.getPrototypeOf(a);

  // 3. 先获取 b 的显示原型
  let bProtoType = b.prototype;

  // 4. 如果原型存在，一直向上查找
  while (proto) {
    // 5. 如果在 a 的原型链上，找到 b 的显示原型
    if (proto === bProtoType) {
      // 6. 返回真
      return true;
    }
    // 7. 如果没有查找到，则继续向上查找
    proto = Object.getPrototypeOf(proto);
  }

  // 8.直至最后没有查找到，直接返回 false
  return false;
}

// 测试代码
console.log(MyInstanceof({}, Object)); // true;
console.log(MyInstanceof(null, Object)); // false;
console.log(MyInstanceof([], Array)); // true;
console.log(MyInstanceof(/ice/, RegExp)); // true;
console.log(MyInstanceof(new Date(), Date)); // true;
console.log(MyInstanceof(1, Number)); // false;
