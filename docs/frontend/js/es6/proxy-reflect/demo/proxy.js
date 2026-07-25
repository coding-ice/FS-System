var obj = {
  name: "ice",
  age: 24,
};

const proxyed = new Proxy(obj, {
  get(target, key, receiver) {
    console.log("get 触发");
    return target[key];
  },
  set(target, key, value, receiver) {
    console.log("set"); // set
    target[key] = value;
  },
  deleteProperty(target, key) {
    console.log("deleteProperty"); // deleteProperty
    return delete target[key];
  },
});

proxyed.address = "Hangzhou";
delete proxyed.address;
