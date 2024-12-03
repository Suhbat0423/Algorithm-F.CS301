class MyQueue {
  constructor() {
    this.stack1 = [];
    this.stack2 = [];
  }
  push(x) {
    this.stack1.push(x);
  }
  pop() {
    if (this.stack2.length === 0) {
      this.transferStack1ToStack2();
    }
    return this.stack2.pop();
  }
  peek() {
    if (this.stack2.length === 0) {
      this.transferStack1ToStack2();
    }
    return this.stack2[this.stack2.length - 1];
  }
  empty() {
    return this.stack1.length === 0 && this.stack2.length === 0;
  }
  transferStack1ToStack2() {
    while (this.stack1.length > 0) {
      this.stack2.push(this.stack1.pop());
    }
  }
}
