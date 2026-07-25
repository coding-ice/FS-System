const info = { name: "ice", age: 25 };

function bar(city, country) {
  // info: ice 25 Hangzhou China
  console.log(`info: ${this.name} ${this.age} ${city} ${country}`);
}

// 传递一个对象，作为 bar 的 this
bar.apply(info, ["Hangzhou", "China"]);

