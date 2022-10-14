# C - covid invections
# L - loss of smell
#
# p(C) = 237118/38268000 ~0.0062
# p(L) = 0.1
# p(L|C) = 0.9
# p(C|L) = p(L|C)p(C) / p(L)
# 1. Take the COVID-19 example from the lecture as a basis and implement a Python class that
# enables to reason from a single effect to the cause. Provide appropriate methods to input
# the required numbers.
# 2. Play with the class, plot output for different combinations of inputs.
# 3. Test the class for p(C)=0.2, P(L)=0.001, P(L|C)=0.01. What happened? Why? How to fix it?

import numpy as np
import matplotlib.pyplot as plt

class Covid19():
    def __init__(self, pc, pl, plc):
        self.pL = pl
        self.pC = pc
        self.pLC = plc
    def answer(self):
        # p(C|L) = p(L|C)p(C) / p(L)
        return (self.pLC * self.pC) / self.pL


Covid = Covid19(0.063, 0.1, 0.9)
print(f'Przykład z wykładu: {Covid.answer():.2%}')

Covid = Covid19(0.2, 0.001, 0.01)
print(f'Przykład dla nowych danych: {Covid.answer():.2%}')

pc_range = np.linspace(0, 1, 100)
ans = []
for pc in pc_range:
    Covid = Covid19(pc, 0.01, 0.9)
    ans.append(Covid.answer())

plt.plot(pc_range, ans)
plt.title('P(C)')
plt.show()

pl_range = np.linspace(0, 0.1, 100)
ans = []
for pl in pl_range:
    Covid = Covid19(0.063, pl, 0.9)
    ans.append(Covid.answer())

plt.plot(pl_range, ans)
plt.title('P(L)')
plt.show()

plc_range = np.linspace(0, 0.9, 100)
ans = []
for plc in plc_range:
    Covid = Covid19(0.063, 0.1, plc)
    ans.append(Covid.answer())

plt.plot(plc_range, ans)
plt.title('P(L|C)')
plt.show()

# pc 0.063 -> 0.2  więcej chorych
# pl 0.1 -> 0.001  mniejsza szansa na utratę węchu (niezależnie od tego czy ma się covid czy nie)
# plc 0.9 -> 0.01  zmniejszamy jak często bycie chorym powoduje utratę węchu
# p(C|L) = p(L|C)p(C) / p(L)

# błąd jest powodowany przez nieprawidłowy związek między parametrami

# jeśli mamy 1000 osób w populacji  to 200 z nich jest chora
# tylko jedna ze wszystkich osób straciła węch
# ale 0,01 z 200 to 2 osoby, z prawdopodobieństwa warunkowego
# czyli 2 osoby w populacji straciły węch ale straciła jedna, mamy sprzeczność

