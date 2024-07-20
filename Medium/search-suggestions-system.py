from pprint import pprint


class Solution(object):
    def suggestedProducts(self, products: list, searchWord: str):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]

        Better solution for time complexity (beats ~51%)
        """
        prod_dict = {}
        for p in sorted(products):
            for i in range(len(p)):
                sub = p[:i+1]
                if sub not in prod_dict:
                    prod_dict[sub] = []
                prod_dict[sub].append(p)

        ret_list = []
        for i in range(len(searchWord)):
            prods = prod_dict.get(searchWord[:i+1], [])
            ret_list.append(prods if len(prods) <= 3 else prods[:3])

        return ret_list

    def solution2(self, products: list, searchWord: str):
        """Better solution for space complexity (beats ~49%)"""
        products.sort()
        ret_list = []
        sub = ''

        for c in searchWord:
            sub += c
            prods = []
            for p in products:
                if len(p) < len(sub):
                    products.pop(p)
            prods = [p for p in products if p.startswith(sub)]
            ret_list.append(prods[:3])

        return ret_list


if __name__ == "__main__":
    sol = Solution()
    tests = [(["mobile", "mouse", "moneypot", "monitor", "mousepad"], "mouse"),
             (["havana"], "havana")]
    for te in tests:
        res = sol.suggestedProducts(*te)
        # res = sol.solution2(*te)
        print(f"{te}:")
        for r in res:
            pprint(r)
