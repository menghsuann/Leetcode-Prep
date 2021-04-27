from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dic
        dic = defaultdict(list)
        #sort and join the string and append back to dic
        for s in strs:
            dic[''.join(sorted(s))].append(s)
        return dic.values()
      #https://www.youtube.com/watch?v=BHC0vgpsl5k
      #https://www.youtube.com/watch?v=Ge04OM0r0d8&t=2s
