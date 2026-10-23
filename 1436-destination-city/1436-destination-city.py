class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        invalids, valids = set(), set()

        for path in paths:
            cityf, cityt = path
            invalids.add(cityf)
            if cityf in valids:
                valids.remove(cityf)
            if cityt in invalids:
                if cityt in valids:
                    valids.remove(cityt)
            else:
                valids.add(cityt)

        return list(valids)[0]
