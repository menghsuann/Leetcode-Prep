from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            #at dic ate sorted category in append eat, tea, ate
            dic[''.join(sorted(s))].append(s)
            #print(s)
        return dic.values()
        
      #https://www.youtube.com/watch?v=BHC0vgpsl5k
      #https://www.youtube.com/watch?v=Ge04OM0r0d8&t=2s
