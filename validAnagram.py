class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sortedS = ''.join(sorted(s))
        sortedT = ''.join(sorted(t))

        if sortedS == sortedT:
            return True
        else:
            return False
