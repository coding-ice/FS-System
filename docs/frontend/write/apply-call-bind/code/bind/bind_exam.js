function bar(city, country) {
  console.log(`info: ${this.name} ${this.age} ${city} ${country}`);
}

const bindBar = bar.bind({ name: "ice", age: 25 }, "Hangzhou");
bindBar("China");
