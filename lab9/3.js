var hasCycle = function (head) {
  let temp = head;
  let slow = head;

  while (temp && temp.next) {
    temp = temp.next.next;
    slow = slow.next;

    if (temp === slow) {
      return true;
    }
  }

  return false;
};
