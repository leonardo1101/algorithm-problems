class Solution(object):
    def pushDominoes(self, dominoes):
        dominoes = list(dominoes)
        list_dom = []
        len_dom = len(dominoes)

        for i in range(len_dom):
            if dominoes[i] != '.':
                list_dom.append(i)
        
        while list_dom:
            len_list = len(list_dom)
            new_list = []
            for i in range(len_list):
                dominoe = list_dom[i]
                if dominoes[dominoe] == "R":
                    if dominoe < len_dom - 1:
                        if dominoes[dominoe + 1] == '.':
                            dominoes[dominoe + 1] = 'R'
                            new_list.append(dominoe + 1)
                        else:
                            if dominoe + 1 in new_list:
                                dominoes[dominoe + 1] = '.'
                elif dominoes[dominoe] == "L":
                    if dominoe > 0:
                        if dominoes[dominoe - 1] == '.':
                            dominoes[dominoe - 1] = 'L'
                            new_list.append(dominoe - 1)
                        else:
                            if dominoe - 1 in new_list:
                                dominoes[dominoe - 1] = '.'
            list_dom = new_list
        return "".join(dominoes)

print Solution().pushDominoes('..R...L..R.')
# ..RR.LL..RR
