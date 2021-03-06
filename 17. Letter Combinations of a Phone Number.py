class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) ==0:
            return []
        digit_map ={
            0:"0",
            1:"1",
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz",
        }
        result = [""]
        for digit in digits:
            temp_list =[]
            for ch in digit_map[int(digit)]:
                for str in result:
                    temp_list.append(str + ch)
            result = temp_list
            
        return result

#https://www.youtube.com/watch?v=KAJnbsikSC8
