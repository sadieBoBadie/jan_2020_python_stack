/* case insensitive string compare */

const strA1 = "ABC";
const strB1 = "abc";
const expected1 = true;

const strA2 = "ABC";
const strB2 = "abd";
const expected2 = false;

const strA3 = "ABC";
const strB3 = "bc";
const expected3 = false;

/**
 * Determines whether or not the strings are equal, ignoring case.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} strA
 * @param {string} strB
 * @return {boolean} If the strings are equal or not.
 */
function caseInsensitiveStringCompare(strA, strB) {

}
// console.log(caseInsensitiveStringCompare(strA1, strB1) == expected1);
// console.log(caseInsensitiveStringCompare(strA2, strB2) == expected2);
// console.log(caseInsensitiveStringCompare(strA3, strB3) == expected3);

module.exports = { caseInsensitiveStringCompare };
