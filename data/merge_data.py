# def intersection(lst1, lst2):
#     lst3 = [value for value in lst2 if value in lst1]
#     return lst3

# with open("dev/seq.in", "r") as f:
#     sequences = []
#     for line in f:
#         sequences.append(line.strip())
# with open("dev-old/seq.in", "r") as f:
#     old_sequences = []
#     for line in f:
#         old_sequences.append(line.strip())

# print("sequences:", len(sequences))
# print("old sequences:", len(old_sequences))
# print("intersection:", len(intersection(sequences, old_sequences)))

with open('./dev-new/intent_label.txt', 'r', encoding='utf-8') as f:
    dev_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-new/slot_label.txt', 'r', encoding='utf-8') as f:
    dev_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
    
with open('./dev-old/intent_label.txt', 'r', encoding='utf-8') as f:
    dev_old_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/label', 'r', encoding='utf-8') as f:
    dev_old_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/seq.in', 'r', encoding='utf-8') as f:
    dev_old_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/seq.out', 'r', encoding='utf-8') as f:
    dev_old_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/slot_label.txt', 'r', encoding='utf-8') as f:
    dev_old_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
    
with open('./dev-old/intent_label.txt', 'r', encoding='utf-8') as f:
    dev_old_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/label', 'r', encoding='utf-8') as f:
    dev_old_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/seq.in', 'r', encoding='utf-8') as f:
    dev_old_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/seq.out', 'r', encoding='utf-8') as f:
    dev_old_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-old/slot_label.txt', 'r', encoding='utf-8') as f:
    dev_old_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
    
with open('./dev-new/intent_label.txt', 'r', encoding='utf-8') as f:
    dev_new_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-new/label', 'r', encoding='utf-8') as f:
    dev_new_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-new/seq.in', 'r', encoding='utf-8') as f:
    dev_new_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-new/seq.out', 'r', encoding='utf-8') as f:
    dev_new_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev-new/slot_label.txt', 'r', encoding='utf-8') as f:
    dev_new_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
    
def get_intersection(a, b):
    return list(set(a).intersection(set(b)))
def get_union(a, b):
    return list(set(a).union(set(b)))
def get_subset(a, b):
    return [c for c in b if c in a]
def get_complementset(a, b):
    return [c for c in b if c not in a]

merge_intent_label = get_union(dev_intent_label, dev_new_intent_label)
merge_slot_label = get_union(dev_slot_label, dev_new_slot_label)
remove_intent_label = get_complementset(merge_intent_label, get_union(dev_old_intent_label, dev_old_intent_label))
remove_slot_label = get_complementset(merge_slot_label, get_union(dev_old_slot_label, dev_old_slot_label))

print(len(merge_intent_label), len(merge_slot_label), len(remove_intent_label), len(remove_slot_label))

merge_dev_label = list()
merge_dev_seqin = list()
merge_dev_seqout = list()
for label, seqin, seqout in zip(dev_old_label, dev_old_seqin, dev_old_seqout):
    if label in remove_intent_label:
        continue
    has_remove_slot_label = False
    for slot_label in seqout.replace('  ', ' ').split(' '):
        if slot_label in remove_slot_label:
            has_remove_slot_label = True
            break
    if has_remove_slot_label:
        continue
    merge_dev_label.append(label)
    merge_dev_seqin.append(seqin)
    merge_dev_seqout.append(seqout)

for label, seqin, seqout in zip(dev_old_label, dev_old_seqin, dev_old_seqout):
    if seqin in merge_dev_seqin:
        continue
    if label in remove_intent_label:
        continue
    has_remove_slot_label = False
    for slot_label in seqout.replace('  ', ' ').split(' '):
        if slot_label in remove_slot_label:
            has_remove_slot_label = True
            break
    if has_remove_slot_label:
        continue
    merge_dev_label.append(label)
    merge_dev_seqin.append(seqin)
    merge_dev_seqout.append(seqout)

for label, seqin, seqout in zip(dev_new_label, dev_new_seqin, dev_new_seqout):
    if seqin in merge_dev_seqin:
        continue
    merge_dev_label.append(label)
    merge_dev_seqin.append(seqin)
    merge_dev_seqout.append(seqout)
    
print(len(dev_new_label), len(dev_old_label), len(dev_old_label), len(dev_new_label) + len(dev_old_label) + len(dev_old_label), len(merge_dev_label))
print(len(dev_new_seqin), len(dev_old_seqin), len(dev_old_seqin), len(dev_new_seqin) + len(dev_old_seqin) + len(dev_old_seqin), len(merge_dev_seqin))
print(len(dev_new_seqout), len(dev_old_seqout), len(dev_old_seqout), len(dev_new_seqout) + len(dev_old_seqout) + len(dev_old_seqout), len(merge_dev_seqout))

import os
if not os.path.exists('./dev/'):
    os.makedirs('./dev/')
with open('./dev/intent_label.txt', 'w', encoding='utf-8') as f:
    for intent_label in merge_intent_label:
        f.write(intent_label + '\n')
with open('./dev/label', 'w', encoding='utf-8') as f:
    for label in merge_dev_label:
        f.write(label + '\n')
with open('./dev/seq.in', 'w', encoding='utf-8') as f:
    for seqin in merge_dev_seqin:
        f.write(seqin + '\n')
with open('./dev/seq.out', 'w', encoding='utf-8') as f:
    for seqout in merge_dev_seqout:
        f.write(seqout + '\n')
with open('./dev/slot_label.txt', 'w', encoding='utf-8') as f:
    for slot_label in merge_slot_label:
        f.write(slot_label + '\n')