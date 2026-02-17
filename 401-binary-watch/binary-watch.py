class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []

        for hh in range(12):
            for mm in range(60):
                if (bin(hh).count("1") + bin(mm).count("1")) == turnedOn:
                    minute = f"{mm:02d}"   # add leading zero if needed
                    res.append(f"{hh}:{minute}")
        
        return res