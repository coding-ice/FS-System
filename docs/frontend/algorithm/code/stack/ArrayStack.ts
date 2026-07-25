import IStack from "./IStack";

class ArrayStack<T = any> implements IStack<T> {
  private data: T[] = [];

  push(value: T) {
    this.data.push(value);
  }

  pop() {
    return this.data.pop();
  }

  peek() {
    return this.data[this.data.length - 1];
  }

  get size() {
    return this.data.length;
  }

  isEmpty() {
    return this.data.length === 0;
  }
}

const stack = new ArrayStack<string>();

stack.push("aaa");
stack.push("bbb");
stack.push("ccc");

console.log(stack.peek());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());

console.log(stack.size);
console.log(stack.isEmpty());
