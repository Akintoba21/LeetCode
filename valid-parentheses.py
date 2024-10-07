class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for x in s:
            if x == '(' or x == '{' or x == '[':
                st.append(x)
            elif x == ')':
                if not st or st[-1] != '(':
                    return False
                else: st.pop(-1)
            elif x == '}':
                if not st or st[-1] != '{':
                    return False
                else: st.pop(-1)
            elif x == ']':
                if not st or st[-1] != '[':
                    return False
                else: st.pop(-1)
        return not st