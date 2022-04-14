def intersection(lst1, lst2):
    lst3 = [value for value in lst2 if value in lst1]
    return lst3

with open("data/syllable-level/train-new/seq.in", "r") as f:
    train_sequences = []
    for line in f:
        train_sequences.append(line.strip())
with open("data/syllable-level/train-old/seq.in", "r") as f:
    train_old_sequences = []
    for line in f:
        train_old_sequences.append(line.strip())

print("train_sequences:", len(train_sequences))
print("train_old_sequences:", len(train_old_sequences))
print("intersection:", intersection(train_sequences, train_old_sequences))