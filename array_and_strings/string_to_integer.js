/**
 * @param {string} str 
 * @return {number}
 */

const INTEGER_LIMIT = Math.pow(2, 31);

let myAtoi = (str) => {
  re = /^[]*(-|\+)?(\d+)+ /;
  matches = str.match(re);

  if (!matches || !matches[1]) {

    return 0;
  }

  integer = parseInt(strNumber);

  if (integer < 0) {

    return Math.max(-INTEGER_LIMIT, integer);
  }

  return Math.min(INTEGER_LIMIT - 1, integer);
};