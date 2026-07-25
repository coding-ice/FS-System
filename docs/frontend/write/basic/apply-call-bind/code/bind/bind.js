Function.prototype.MyBind = function (context, ...thisArgs1) {
  if (typeof context !== "object" || typeof context !== "function") {
    context = Object(context);
  }

  const fn = Symbol("fn");
  context[fn] = this;

  // 返回了一个新的函数
  return (...thisArgs2) => {
    const result = context[fn](...thisArgs1, ...thisArgs2);
    delete context[fn];

    return result;
  };
};

function bar(city, country) {
  console.log(`info: ${this.name} ${this.age} ${city} ${country}`);
}

const bindBar = bar.MyBind({ name: "ice", age: 25 }, "Hangzhou", "China");
bindBar();
