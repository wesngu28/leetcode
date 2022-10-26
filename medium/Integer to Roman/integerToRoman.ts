function intToRoman(num: number): string {
    const numerals = {
        '1' : 'I',
        '5' : 'V',
        '4' : 'IV',
        '10' : 'X',
        '9' : 'IX',
        '50' : 'L',
        '40' : 'XL',
        '100' : 'C',
        '90' :'XC',
        '500' : 'D',
        '400' : 'CD',
        '1000' : 'M',
        '900' : 'CM'
    }
    let current = num
    let total = ''
    const iterateMe = Object.keys(numerals)
    for (let i = iterateMe.length-1; i >= 0; i--) {
        if (current % Number(iterateMe[i]) !== current) {
            let constituents = Math.floor(current/Number(iterateMe[i]))
            if (constituents === 0) constituents = 1
            for (let j = 0; j < constituents; j++) {
                total += numerals[String(iterateMe[i])]
            }
            current -= constituents * Number(iterateMe[i])
        }
    }
    return String(total)
};

/* O(n^2) run time as two iterations, one of numerals and one of the matches must be made,
but the last iteration should not be as long in an overall real-world case but is still
o(n^2) in a worst-case analysis
*/
