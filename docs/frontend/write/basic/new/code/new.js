function Info(name, age) {
  this.name = name;
  this.age = age;
}

function MyNew(Fn, ...args) {
  // 1. 创建一个新对象
  const obj = {};
  // 2. obj.__proto__ = Fn.prototype
  Object.setPrototypeOf(obj, Fn.prototype);

  // 3. Fn 函数的 this，修改为 obj，并且执行代码
  const result = Fn.apply(obj, args);

  // 4. 如果是 object 类型，或者是 func 类型，返回 result
  if (
    (typeof result === "object" && result !== null) ||
    typeof result === "function"
  )
    return result;

  // 5. 否则，返回 result 对象
  return obj;
}

// {name: 'ice', age: 25}
const res = MyNew(Info, "ice", 25);
