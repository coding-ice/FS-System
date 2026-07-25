function foo() {
  for (let i = 0; i < 1000000000; i++) {
    if (i === 1000000000 / 2) {
      console.log("a2 -> foo");
    }
  }
}
foo();
