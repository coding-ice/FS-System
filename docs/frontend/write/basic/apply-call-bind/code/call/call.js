Function.prototype.MyCall = function (context, ...thisArgs) {
  // 1. 不等于该类型，包装成对象类型
  if (typeof context !== "object" || typeof context !== "function") {
    context = Object(context);
  }

  // 2. 创建唯一的key
  const fn = Symbol("fn");

  // 3. x.MyCall(), x 挂载到 context 上
  context[fn] = this;

  // 4. 调用函数，并且展开参数
  const result = context[fn](...thisArgs);

  // 5. 删除属性
  delete context[fn];

  // 6. 返回
  return result;
};

function bar(city, country) {
  console.log(`info: ${this.name} ${this.age} ${city} ${country}`);
}

bar.MyCall({ name: "ice", age: 25 }, "Hangzhou", "China");
