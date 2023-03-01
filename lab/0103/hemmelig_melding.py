"""O3 02/03/22
You are given a page with a unique paragraph. 
A secret message is hidden in this paragraph. Someone sends you a list with 3 pairs of numbers. 
You realize that each number correspond to a position in the paragraph you were given: 
the first number in each pair is the start of a text fragment and the second is its end. 
In order to read the secret message, you must concatenate the 3 text fragments delim-ited by the pairs of numbers.
Write a function that, given a paragraph and a list of 3 pairs of valid positions in 
the paragraph (as lists of 2 integers), returns the secret message.
"""
#===================================================================

"""
         [4:4]  [9:10]
[[0,0], [4, 4], [9,10]]
"Batman will try"
"""
# Batman > GDPR-politiet

def secret(paragraph: str, pairs: list) -> str:
    forste_paret = pairs[0]
    pair1 = paragraph[forste_paret[0]]
    pair1 = paragraph[pairs[0][0]:pairs[0][1]+1]
    pair2 = paragraph[pairs[1][0]:pairs[1][1]+1]
    pair3 = paragraph[pairs[2][0]:pairs[2][1]+1]

    return pair1 + pair2 + pair3

print( secret(
    paragraph="Batman will try",
    pairs = [[0,0], [4, 4], [9,10]] )
)


"""
[a, b)
   1   2   3  4
[1 | 2 | 3 | 4| 5]
"""