# Reason from multiple evidence
# 1. Take the burglary example from the lecture as a basis and implement a Python class that
# enables to reason from any number of pieces of evidence. Provide appropriate methods to
# define the number of evidence pieces and input the required numbers. Ensure proper
# operation when some of the pieces of evidence are not present.
# 2. Play with the class, plot output for different combinations of inputs.
# 3. Going back to the example, consider situation when the alarm is not silent – it blares horn
# and flashes lig
import numpy as np
import matplotlib.pyplot as plt


class burglar():
    def __init__(self, pi, pa, pb, pai, pbi):
        self.alarm = None
        self.dog = None
        self.pi = pi  # : average ratio of the houses that are burgled during the night to the total houses
        self.pa = pa  # for my alarm: ratio of the nights it goes off to the nights in the assumed time period; it goes off twice a night so rarely we may treat is as a single event
        self.pb = pb  # for my neighbour’s dog: ratio of the days he barks during the night to the nights in the assumed time period
        self.pai = pai  # probability of alarm going on if burglary takes place
        self.pbi = pbi  # probability of dog barking when burglary takes place

    def alarm_status(self, status):
        self.alarm = status

    def dog_status(self, status):
        self.dog = status

    def answer(self):
        if self.dog is None and self.alarm:
            # p(I|A)
            return (self.pai * self.pi) / self.pa

        if self.dog and self.alarm:
            return (self.pbi / self.pb) * ((self.pai * self.pi) / self.pa)

        if self.alarm and not self.dog:
            return ((1 - self.pbi) / (1 - self.pb)) * ((self.pai * self.pi) / self.pa)

        if self.alarm is None and self.dog:
            # p(I|B)
            return (self.pbi * self.pi) / self.pb

        if self.dog and not self.alarm:
            return (1 - self.pai) / (1 - self.pa) * ((self.pbi * self.pi) / self.pb)


print('data from lecture:')
isburglary = burglar(0.002, 0.01, 0.5, 0.8, 0.98)
isburglary.alarm_status(True)
isburglary.dog_status(None)
print(f'alarm on but dont know if dog is barking: {isburglary.answer():.2%}')

isburglary.alarm_status(True)
isburglary.dog_status(True)
print(f'alarm on and dog barking: {isburglary.answer():.2%}')

isburglary.alarm_status(True)
isburglary.dog_status(False)
print(f'alarm on but dog not barking: {isburglary.answer():.2%}')

isburglary.alarm_status(None)
isburglary.dog_status(True)
print(f'Dog barking but dont know if alarm is on: {isburglary.answer():.2%}')

isburglary.alarm_status(False)
isburglary.dog_status(True)
print(f'Dog barking and alarm is off: {isburglary.answer():.4%}')

isburglary.alarm_status(True)
isburglary.dog_status(True)
print(f'Dog barking but dont know if alarm is on: {isburglary.answer():.2%}')

print('')
print('Much better alarm P(A|I)=0.95')
isburglary = burglar(0.002, 0.01, 0.5, 0.95, 0.98)
isburglary.alarm_status(True)
isburglary.dog_status(None)
print(f'alarm on but dont know if dog is barking: {isburglary.answer():.2%}')

isburglary.alarm_status(True)
isburglary.dog_status(True)
print(f'alarm on and dog barking: {isburglary.answer():.2%}')

isburglary.alarm_status(True)
isburglary.dog_status(False)
print(f'alarm on but dog not barking: {isburglary.answer():.2%}')

isburglary.alarm_status(None)
isburglary.dog_status(True)
print(f'Dog barking but dont know if alarm is on: {isburglary.answer():.2%}')

isburglary.alarm_status(False)
isburglary.dog_status(True)
print(f'Dog barking and alarm is off: {isburglary.answer():.4%}')

isburglary.alarm_status(True)
isburglary.dog_status(True)
print(f'Dog barking but dont know if alarm is on: {isburglary.answer():.2%}')



x = np.linspace(0, 1, 100)
ans = []
for i in x:
    isburglary = burglar(0.002, 0.01, 0.5, 0.95, i)
    isburglary.alarm_status(True)
    isburglary.dog_status(True)
    ans.append(isburglary.answer())
plt.plot(x, ans, label='Dog barking and alarm on')


ans = []
for i in x:
    isburglary = burglar(0.002, 0.01, 0.5, 0.95, i)
    isburglary.alarm_status(False)
    isburglary.dog_status(True)
    ans.append(isburglary.answer())
plt.plot(x, ans, label='Dog barking and alarm not on')

ans = []
for i in x:
    isburglary = burglar(0.002, 0.01, 0.5, 0.95, i)
    isburglary.alarm_status(None)
    isburglary.dog_status(True)
    ans.append(isburglary.answer())
plt.plot(x, ans, label='Dog barking and dont know if alarm is on or off')

plt.title('Probability of burglary')
plt.ylabel('Probabilty')
plt.xlabel('probability of dog barking when burglary takes place')
# plt.yscale('log')
plt.legend()
plt.show()



x = np.linspace(0.7, 1, 100)
ans = []
for i in x:
    isburglary = burglar(0.002, 0.01, 0.5, i, 0.98)
    isburglary.alarm_status(True)
    isburglary.dog_status(True)
    ans.append(isburglary.answer())
plt.plot(x, ans, label='Alarm on and dog barking')


ans = []
for i in x:
    isburglary = burglar(0.002, 0.01, 0.5, 0.95, i)
    isburglary.alarm_status(False)
    isburglary.dog_status(False)
    ans.append(isburglary.answer())
plt.plot(x, ans, label='Alarm off and dog not barking')

ans = []
for i in x:
    isburglary = burglar(0.002, 0.01, 0.5, 0.95, i)
    isburglary.alarm_status(True)
    isburglary.dog_status(None)
    ans.append(isburglary.answer())
plt.plot(x, ans, label='Alarm on and don\'t know abaout dog')

plt.title('Probability of burglary')
plt.ylabel('Probabilty')
plt.xlabel('probability of alarm turning on when burglary takes place')
# plt.yscale('log')
plt.legend()
plt.show()
