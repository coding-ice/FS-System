var obj = {
  name: "ice",
  age: 24,
};

var objName = obj.name;

Object.defineProperty(obj, "name", {
  get() {
    console.log("get 触发");
    return objName;
  },
  set(newValue) {
    console.log("set 触发");
    objName = newValue;
  },
});

obj.name = "panda";
console.log(obj.name);

/**
 * set 触发
 * get 触发
 * panda
 */
