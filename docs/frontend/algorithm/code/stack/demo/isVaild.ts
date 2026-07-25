// 20. 有效的括号

function isValid(s: string): boolean {
  if (s.length % 2 !== 0) return false;

  const stack: string[] = [];
  const bracketMap: Record<string, string> = {
    "(": ")",
    "[": "]",
    "{": "}",
  };
  const leftBracket = Object.keys(bracketMap);

  for (let char of s) {
    if (leftBracket.includes(char)) {
      stack.push(bracketMap[char]);
    } else {
      if (stack.pop() !== char) return false;
    }
  }

  return !stack.length;
}

console.log(isValid("()[]{}"));
console.log(isValid("(]"));
console.log(isValid("([])"));
