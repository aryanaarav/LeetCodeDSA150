from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = defaultdict(list)
        for string in strs:

            count = [0] * 26

            for c in string:

                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(string) # here we are creating a tuple of counts instead of a list as a list is 
                                             # mutable and keys of a dict can't be mutable therefore tuples are immutable
                                             # and hence are used instead

        return res.values()