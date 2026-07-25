const obj = {
  name: "ice",
  age: 24,
  get address() {
    console.log(this === proxyed); // true
    return "Hangzhou";
  },
};

const proxyed = new Proxy(obj, {
  get(target, key, receiver) {
    return Reflect.get(target, key, receiver);
  },
  set(target, key, value, receiver) {
    console.log("set"); // set
    return Reflect.set(target, key, value, receiver);
  },
  deleteProperty(target, key) {
    console.log("del"); // del
    return Reflect.deleteProperty(target, key);
  },
});
