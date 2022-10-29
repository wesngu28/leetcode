/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
 var findSubstring = function(s, words) {
    const interval = words[0].length
    const expectedLen = interval * words.length
    let startingIndices = []
    for (let i = 0; i <= s.length-1; i++) {
        let splitArr = [];
        for(let j = i; j < i + expectedLen; j += interval) {
            splitArr.push(s.slice(j, j+interval))
        }
        const sorted = splitArr.sort()
        const wordSort = words.sort()
        let yesValues = 0
        let please = true
        for(let b = 0; b < sorted.length; b ++) {
            if((sorted[b] === wordSort[b]) === false) {
                please = false
                b = sorted.length
            }
        }
        if (please) startingIndices.push(i)
    }
    return startingIndices
};