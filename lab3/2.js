/**
 * @param {string} s
 * @return {string}
 */
var longestNiceSubstring = function (s) {
  return divideAndConquer(s, 0, s.length - 1);
};

function divideAndConquer(s, start, end) {
  if (end - start < 1) {
    return "";
  }

  const charSet = new Set(s.slice(start, end + 1));

  for (let i = start; i <= end; i++) {
    const ch = s[i];

    if (!charSet.has(ch.toLowerCase()) || !charSet.has(ch.toUpperCase())) {
      const leftResult = divideAndConquer(s, start, i - 1);
      const rightResult = divideAndConquer(s, i + 1, end);

      return leftResult.length >= rightResult.length ? leftResult : rightResult;
    }
  }

  return s.slice(start, end + 1);
}
