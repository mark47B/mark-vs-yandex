# Not full
# На сколько можно наполнить стакан?
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *,*,*,*,*,*,*,*
# Ответ 42

# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
#  , , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *,*,*,*,*,*,*,*
#  Ответ 12, т.к. отверстие сбоку

# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *, , , , , , ,*
# *,*,*,*, ,*,*,*

# Ответ 0, т.к. отверстие снизу

from sys import stdin
def get_voluume():
    input_end = ''
    volume = 0
    line = str()
    hole = False
    end = False
    for line in stdin.read().splitlines():
            if end is False:
                new_volume = 0
                for i in range(len(line)):
                    if line[i] == ",":
                        continue
                    if (i == 0 or i == len(line)-1) and line[i] == " ":
                        volume = 0
                        hole = True
                        break
                    if line[i] == " ":
                        new_volume += 1
                        continue
                    if line[i] == "*":
                        continue
                if hole is True:
                    volume = 0
                    hole = False
                    continue
                if new_volume == 0:
                    end = True
                    #  return volume
                else:
                    volume += new_volume
    if end is False:
        for i in range(len(line)):
            if line[i] == "*":
                continue
            if line[i] == ",":
                continue
            if line[i] == " ":
                return 0

    return volume

print(get_voluume())
