Function.prototype.MyApply = function (context, arrayArgs) {
  // 1. 如果不是这些类型，把它包装为 Obj 类型
  if (typeof context !== "object" || typeof context !== "function") {
    context = Object(context);
  }

  // 2. 创建一个 symbol 属性，防止重复
  const fn = Symbol("fn");

  // 3. x.myApply() 隐式绑定，函数体内的 this 指向 x
  context[fn] = this;

  // 4. x 函数挂在了 context 上，所以内部的 this 指向已经变为 ctx
  const result = context[fn](...arrayArgs);

  // 5. 删除附加的 symbol
  delete context[fn];

  // 6. 返回返回值
  return result;
};

const info = { name: "ice", age: 25 };

function bar(city, country) {
  console.log(`info: ${this.name} ${this.age} ${city} ${country}`);
}

bar.MyApply(info, ["Hangzhou", "China"]);
