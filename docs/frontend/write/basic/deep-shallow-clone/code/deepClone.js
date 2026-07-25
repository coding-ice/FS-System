function deepClone(target, map = new WeakMap()) {
  // 1. 处理简单数据类型 或者 null
  if (target === null || typeof target !== "object") {
    return target;
  }

  // 2. 边界处理，也可以是 Map 等类型
  if (target instanceof Set) {
    const newSet = new Set();
    target.forEach((v) => {
      newSet.add(v);
    });

    return newSet;
  }

  // 3. 创建新的对象或者数组
  const newObject = Array.isArray(target) ? [] : {};

  // 4. 用于解决循环引用问题
  if (map.has(target)) {
    return map.get(target);
  }
  map.set(target, newObject);

  // 5. 遍历
  for (let key in target) {
    // 6. 找到自身属性
    if (Object.prototype.hasOwnProperty.call(target, key)) {
      // 7. 递归调用或去新的值或者引用
      newObject[key] = deepClone(target[key], map);
    }
  }

  // 8. 返回 clone 后的对象
  return newObject;
}
