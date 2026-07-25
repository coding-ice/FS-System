import IStack from "./IStack";

class ListNode<T> {
  public next: ListNode<T> | null;

  constructor(public value: T) {
    this.next = null;
  }
}

class LinkedListStack<T> implements IStack<T> {
  // head -> 栈顶
  private head: ListNode<T> | null = null;
  private stackSize: number = 0;

  push(value: T): void {
    const node = new ListNode(value);
    node.next = this.head;
    this.head = node;

    this.stackSize++;
  }

  pop(): T | undefined {
    if (!this.head) return;

    const value = this.head.value;
    this.head = this.head.next;
    this.stackSize--;

    return value;
  }

  peek(): T | undefined {
    return this.head?.value;
  }

  isEmpty(): boolean {
    return this.size === 0;
  }

  get size() {
    return this.stackSize;
  }
}

const stack = new LinkedListStack<number>();
stack.push(1);
stack.push(2);
stack.push(3);

console.log(stack.peek());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.pop());
console.log(stack.size);
console.log(stack.isEmpty());
