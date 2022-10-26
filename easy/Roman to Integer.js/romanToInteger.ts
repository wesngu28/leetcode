function romanToInt(s: string): number {
    const numerals = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000,
    }
    
    let total = 0
    
    for (let i = s.length-1; i >= 0; i--) {
        if (i === 0) return total += numerals[s[i]]
        if (numerals[s[i]] <= numerals[s[i-1]]) {
            total += numerals[s[i]]
        } else {
            total += numerals[s[i]] - numerals[s[i-1]]
            i--
        }
    }
    
    return total
};

// O(n) worst-case