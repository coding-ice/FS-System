interface IStack<T> {
  push(value: T): void;
  pop(): T | undefined;
  peek(): T | undefined;
  size: number;
  isEmpty(): boolean;
}

export default IStack;
