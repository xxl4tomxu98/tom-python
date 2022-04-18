'''is_shuffle?
Given three strings, return whether the third is an interleaving of the first two.
Interleaving means it only contains characters from the other two, no more no less, 
and preserves their character ordering. "abdecf" is an interleaving of "abc" and "def". 
Note that the first two strings needn't be in alphabetical order like these.

You may assume that the first two strings do not contain any characters in common.
Next, relax the assumption that the first two strings contain no overlap. Analyze
the time-complexity of your solution. You may wish to view this problem recursively.

Method Signature
is_shuffle(str1, str2, str3)

Example input/output
is_shuffle?('XXZ', 'XXY', 'XXYXXZ')
=> true
Note, make sure you can answer why this won't work with your initial implementation.'''

# time: O(n), space: O(1) but does not consider repeats, won't work
def is_shuffle(str1, str2, str3):
    if not(len(str1) + len(str2) == len(str3)):
        return False
    # create 3 pointers traversing all 3 lists
    idx1, idx2, idx3 = 0, 0, 0
    while idx3 < len(str3):
        if str1[idx1] == str3[idx3]:
            # match: good! go to next step
            idx1 += 1
            idx3 += 1
        elif str2[idx2] == str3[idx3]:
            idx2 += 1
            idx3 += 1
        else:
            return False        
    return True

print(is_shuffle('XXZ', 'XXY', 'XXYXXZ'))


# when we allow repeats in str1 and str2
'''Imagine that we try to use our initial solution with our first implementation of is_shuffle?.
 Why could interleaving?('XXZ', 'XXY', 'XXYXXZ') return false? By default, if we find a matching 
 letter in our first string, we step forward with that index. When we get to the Y in our 
 interleaved string, we are still at the first index of the second string will return false. 
 We can resolve this problem by making two recursive calls if both strings match a letter - one 
 where we step forward in the first string, one where we step forward in the second. If either of
 these finds an interleaving string, we return true immediately. 
 (Our base case is that all strings are empty, meaning that we've stepped through every letter.) 
 Otherwise, if neither possibility is interleaving, we return false. In this case, we make 2 
 recursive calls for each letter in our interleaving string, for a worst case performance of O(2**n).'''
def is_shuffle1(str1, str2, str3):
    if len(str3) == 0:
        return (len(str1)==0) & (len(str2)==0)

    if str1[0] == str3[0]:
        if is_shuffle(str1[1:], str2, str3[1:]):
            return True
    
    if str2[0] == str3[0]:
        if is_shuffle(str1, str2[1:], str3[1:]):
            return True
    return False

print(is_shuffle1('XXZ', 'XXY', 'XXYXXZ'))


# BST solution dynamic
def is_shuffle2(str1, str2, str3):
    candidates = [[0,0]]
    while (len(candidates) != 0):
        temp = candidates.pop(0)
        str1_used_len = candidates[0]
        str2_used_len = candidates[1]
        str3_used_len = str1_used_len + str2_used_len
        if str3_used_len == len(str3):
            return True        
        if str1[str1_used_len] == str3[str3_used_len]:
            candidates.push([str1_used_len + 1, str2_used_len])        
        if str2[str2_used_len] == str3[str3_used_len]:
            candidates.push([str1_used_len, str2_used_len + 1])

print(is_shuffle2('XXZ', 'XXY', 'XXYXXZ'))       

def is_shuffle3(str1, str2, str3):
    seen_candidates = {}
    candidates = [[0,0]]
    while (len(candidates) != 0):
        temp = candidates.pop(0)
        str1_used_len = candidates[0]
        str2_used_len = candidates[1]
        str3_used_len = str1_used_len + str2_used_len
        if (str3_used_len == str3.length):
            return True        
        if (str1[str1_used_len] == str3[str3_used_len]):
            new_candidate = [str1_used_len + 1, str2_used_len]
            if (not seen_candidates[new_candidate]):
                candidates.push(new_candidate)
                seen_candidates[new_candidate] = True        
        if (str2[str2_used_len] == str3[str3_used_len]):
            new_candidate = [str1_used_len, str2_used_len + 1]
            if (not seen_candidates[new_candidate]):
                candidates.push(new_candidate)
                seen_candidates[new_candidate] = True  
    return False
 
print(is_shuffle3('XXZ', 'XXY', 'XXYXXZ'))