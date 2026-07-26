function shallowClone(target) {
  // 1. 处理基本数据类型 和 null
  if (target === null || typeof target !== "object") {
    return target;
  }

  // 2. 创建一个新的对象
  const newObject = {};

  // 3. 遍历
  for (let key in target) {
    // 4. 如果是其自身对象中的属性
    if (Object.prototype.hasOwnProperty.call(target, key)) {
      // 5. 直接赋值给新对象
      newObject[key] = target[key];
    }
  }

  // 6. 返回新的对象
  return newObject;
}
