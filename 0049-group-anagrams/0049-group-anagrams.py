# class Solution:
#     def groupAnagrams(self, strg = list[str]):
#         group = {}
#         for word in strg:
#             sort_word = ''.join(sorted(word))
#             if sort_word in group:
#                 group[sort_word].append(word)
#             else:
#                 group[sort_word] = (word)
#         return list (group.values())

class Solution:
    def groupAnagrams(self, strs: list[str]):
        group = {}
        for word in strs:
            sort_word = ''.join(sorted(word))
            if sort_word in group:
                group[sort_word].append(word)
            else:
                group[sort_word] = [word]
        return list (group.values())
