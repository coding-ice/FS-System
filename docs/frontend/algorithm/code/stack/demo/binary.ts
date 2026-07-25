function binary(n: number): string {
  const stack = [];

  let value = n;

  while (value > 0) {
    const remainder = value % 2;
    stack.push(remainder);
    value = Math.floor(value / 2);
  }

  let str = "";

  while (stack.length) {
    str += stack.pop();
  }

  return str;
}

console.log(binary(100));

/*
  不断的 / 2 取余数
  10 / 2 = 0
  5 / 2 = 1
  2 / 2 = 0
  1 / 0 = 1
  0

  [1,0,1,0]
*/
