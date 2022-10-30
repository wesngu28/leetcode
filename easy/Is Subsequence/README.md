I overthought this one substantially.

My thought process was iterate through the entirety of the first string to find matches, and store the matches with their index in a hashtable.
The index would start at the highest index in the hashtable to make sure the order was maintained, however, this failed to account for strings like
'aaaaaa' trying to be a subsequence of 'bbaaaa', as the way I did it, I could not figure out a way to account for string lengths.

Two pointers makes a lot more sense than the witchcraft I was doing.