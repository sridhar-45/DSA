# class Solution:
#     def readBinaryWatch(self, turnedOn: int) -> List[str]:
#         res = []

#         for hh in range(12):
#             for mm in range(60):
#                 if (bin(hh).count("1") + bin(mm).count("1")) == turnedOn:
#                     minute = f"{mm:02d}"   # add leading zero if needed
#                     res.append(f"{hh}:{minute}")
        
#         return res


class Solution:
    def readBinaryWatch(self, turnedOn: int):
        return [
            f"{h}:{m:02d}"
            for h in range(12)
            for m in range(60)
            if (h.bit_count() + m.bit_count()) == turnedOn
        ]
