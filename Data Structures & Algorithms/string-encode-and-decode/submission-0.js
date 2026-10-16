class Solution {
  // Encodes a list of strings to a single string.
  encode(strs) {
    // We'll use the length of each string + '#' as a separator
    // Example: ["ram", "hut"] => "3#ram3#hut"
    return strs.map(str => str.length + '#' + str).join('');
  }

  // Decodes a single string to a list of strings.
  decode(s) {
    const res = [];
    let i = 0;

    while (i < s.length) {
      // find separator '#'
      let j = i;
      while (s[j] !== '#') j++;

      // get length of next string
      const length = parseInt(s.slice(i, j));

      // move after '#', then get next string
      const word = s.slice(j + 1, j + 1 + length);
      res.push(word);

      // move i pointer to next encoded segment
      i = j + 1 + length;
    }

    return res;
  }
}
