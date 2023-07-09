class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        t1 = list(t)
        s1 = list(s)
        t1.sort()
        s1.sort()
        return ((s1) == (t1))
        