class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        from collections import defaultdict  # To use defaultdict, which provides a default value for nonexistent keys.

        anagram = defaultdict(list)  # 'anagram' is a dictionary where each key is a sorted tuple of characters, and the values are lists of strings (anagrams).
        result = []  # 'result' is a list that will store the final groups of anagrams.

        for s in strs:  # Iterate through each string 's' in the input list 'strs'.
            sortstrs = tuple(sorted(s))  # 'sortstrs' is a tuple containing the sorted characters of the string 's'.
            anagram[sortstrs].append(s)  # Add the original string 's' to the list of its sorted representation in the 'anagram' dictionary.

        for value in anagram.values():  # Iterate through the lists of anagrams in the dictionary.
            result.append(value)  # Add each list of anagrams to the result.

        return result  # Return the result list containing groups of anagrams.
