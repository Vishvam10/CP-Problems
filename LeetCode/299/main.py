class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        sm, gm = {}, {}
        b, c = 0, 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
            else:
                if secret[i] in sm:
                    sm[secret[i]] += 1
                else:
                    sm[secret[i]] = 1
                if guess[i] in gm:
                    gm[guess[i]] += 1
                else:
                    gm[guess[i]] = 1
        for i in gm:
            if i in sm:
                c += min(sm[i], gm[i])

        return "{}A{}B".format(b, c)
                