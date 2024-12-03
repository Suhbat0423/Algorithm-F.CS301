class MyStack {
  constructor() {
    this.a = [];
  }

  push(x) {
    this.a.push(x);
    for (let i = 0; i < this.a.length - 1; i++) {
      this.a.push(this.a.shift());
    }
  }

  pop() {
    return this.a.shift();
  }

  top() {
    return this.a[0];
  }

  empty() {
    return this.a.length === 0;
  }
}
