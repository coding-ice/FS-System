var obj = {
  name: "ice",
  age: 24,
};

Object.keys(obj).forEach((key) => {
  var value = obj[key];
  Object.defineProperty(obj, key, {
    get() {
      return value;
    },
    set(newValue) {
      value = newValue;
    },
  });
});

obj.name = "panda";
console.log(obj.name);
