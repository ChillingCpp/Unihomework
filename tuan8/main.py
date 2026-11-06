import random

def rng(a:int , b:int ) -> int:
    return random.randint(a, b)

def to1d(a: list[list]) -> list:
    b = []
    for i in a:
        for j in i:
            b.append(j)
    return b
def freq(a: list) -> dict:
    b = {}
    for i in a:
        b[i] = b.get(i, 0) + 1
    return b


def rdfile(path: str):
    if not path.endswith(".txt"):
        return
    with open(path, 'r', encoding='utf-8') as f:
        print(f.read())

def splt(a: str) -> list[str]:
    return a.split()

def countf(txt: str, pat: str) -> int:
    lps = [0 for i in range(len(pat))]
    for i in range(1, len(pat)):
        j = lps[i-1]
        while pat[i] != pat[j] and j > 0:
            j = lps[j-1]
        lps[i] = j + (pat[i] == pat[j])
    j = 0
    cnt= 0
    for i in range(0, len(txt)):
        while (j > 0 and txt[i] != pat[j]): 
            j = lps[j-1]
        if (txt[i] == pat[j]):
            j += 1
        if (j == len(pat)):
            cnt+=1
            j = lps[j-1]
    return cnt


