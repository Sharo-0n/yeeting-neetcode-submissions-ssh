class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # convert each str to [0]*26 -> delim str
        converted_strs = {} # converted_str: [original_str]
        for s in strs:
            temp = [0]*26
            for ch in s:
                temp[ord(ch) - ord('a')] += 1
            key = ','.join(map(str,temp))
            if key in converted_strs:
                converted_strs[key].append(s)
            else:
                converted_strs[key] = [s]
        
        ret_list = []
        for k in converted_strs.keys():
            ret_list.append(converted_strs[k])

        return ret_list
        # tc big o m*n / total # char
        # sc big o # elem (because constant length of 26)