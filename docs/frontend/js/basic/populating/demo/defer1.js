function baz() {
  for (let i = 0; i < 1000000000; i++) {
    if (i === 1000000000 / 2) {
      console.log("d1 -> bar");
    }
  }
}
baz();
