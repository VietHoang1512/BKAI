def intersection(lst1, lst2):
    lst3 = [value for value in lst2 if value in lst1]
    return lst3


with open("train-new/seq.in", "r") as f:
    train_sequences = []
    for line in f:
        train_sequences.append(line.strip())
with open("train/seq.in", "r") as f:
    train_old_sequences = []
    for line in f:
        train_old_sequences.append(line.strip())

print("train_sequences:", len(train_sequences))
print("train_old_sequences:", len(train_old_sequences))
print("intersection:", len(intersection(train_sequences, train_old_sequences)))

# with open('./dev/intent_label.txt', 'r', encoding='utf-8') as f:
#     dev_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev/label', 'r', encoding='utf-8') as f:
#     dev_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev/seq.in', 'r', encoding='utf-8') as f:
#     dev_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev/seq.out', 'r', encoding='utf-8') as f:
#     dev_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev/slot_label.txt', 'r', encoding='utf-8') as f:
#     dev_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

# with open('./dev-old/intent_label.txt', 'r', encoding='utf-8') as f:
#     dev_old_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev-old/label', 'r', encoding='utf-8') as f:
#     dev_old_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev-old/seq.in', 'r', encoding='utf-8') as f:
#     dev_old_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev-old/seq.out', 'r', encoding='utf-8') as f:
#     dev_old_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./dev-old/slot_label.txt', 'r', encoding='utf-8') as f:
#     dev_old_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

# with open('./train-old/intent_label.txt', 'r', encoding='utf-8') as f:
#     train_old_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-old/label', 'r', encoding='utf-8') as f:
#     train_old_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-old/seq.in', 'r', encoding='utf-8') as f:
#     train_old_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-old/seq.out', 'r', encoding='utf-8') as f:
#     train_old_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-old/slot_label.txt', 'r', encoding='utf-8') as f:
#     train_old_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

# with open('./train-new/intent_label.txt', 'r', encoding='utf-8') as f:
#     train_new_intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-new/label', 'r', encoding='utf-8') as f:
#     train_new_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-new/seq.in', 'r', encoding='utf-8') as f:
#     train_new_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-new/seq.out', 'r', encoding='utf-8') as f:
#     train_new_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
# with open('./train-new/slot_label.txt', 'r', encoding='utf-8') as f:
#     train_new_slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

# def get_intersection(a, b):
#     return list(set(a).intersection(set(b)))
# def get_union(a, b):
#     return list(set(a).union(set(b)))
# def get_subset(a, b):
#     return [c for c in b if c in a]
# def get_complementset(a, b):
#     return [c for c in b if c not in a]

# merge_intent_label = get_union(dev_intent_label, train_new_intent_label)
# merge_slot_label = get_union(dev_slot_label, train_new_slot_label)
# remove_intent_label = get_complementset(merge_intent_label, get_union(dev_old_intent_label, train_old_intent_label))
# remove_slot_label = get_complementset(merge_slot_label, get_union(dev_old_slot_label, train_old_slot_label))

# print(len(merge_intent_label), len(merge_slot_label), len(remove_intent_label), len(remove_slot_label))

# merge_train_label = list()
# merge_train_seqin = list()
# merge_train_seqout = list()
# for label, seqin, seqout in zip(dev_old_label, dev_old_seqin, dev_old_seqout):
#     if label in remove_intent_label:
#         continue
#     has_remove_slot_label = False
#     for slot_label in seqout.replace('  ', ' ').split(' '):
#         if slot_label in remove_slot_label:
#             has_remove_slot_label = True
#             break
#     if has_remove_slot_label:
#         continue
#     merge_train_label.append(label)
#     merge_train_seqin.append(seqin)
#     merge_train_seqout.append(seqout)

# for label, seqin, seqout in zip(train_old_label, train_old_seqin, train_old_seqout):
#     if seqin in merge_train_seqin:
#         continue
#     if label in remove_intent_label:
#         continue
#     has_remove_slot_label = False
#     for slot_label in seqout.replace('  ', ' ').split(' '):
#         if slot_label in remove_slot_label:
#             has_remove_slot_label = True
#             break
#     if has_remove_slot_label:
#         continue
#     merge_train_label.append(label)
#     merge_train_seqin.append(seqin)
#     merge_train_seqout.append(seqout)

# for label, seqin, seqout in zip(train_new_label, train_new_seqin, train_new_seqout):
#     if seqin in merge_train_seqin:
#         continue
#     merge_train_label.append(label)
#     merge_train_seqin.append(seqin)
#     merge_train_seqout.append(seqout)

# print(len(train_new_label), len(train_old_label), len(dev_old_label), len(train_new_label) + len(train_old_label) + len(dev_old_label), len(merge_train_label))
# print(len(train_new_seqin), len(train_old_seqin), len(dev_old_seqin), len(train_new_seqin) + len(train_old_seqin) + len(dev_old_seqin), len(merge_train_seqin))
# print(len(train_new_seqout), len(train_old_seqout), len(dev_old_seqout), len(train_new_seqout) + len(train_old_seqout) + len(dev_old_seqout), len(merge_train_seqout))

# import os
# if not os.path.exists('./merge-train/'):
#     os.makedirs('./merge-train/')
# with open('./merge-train/intent_label.txt', 'w', encoding='utf-8') as f:
#     for intent_label in merge_intent_label:
#         f.write(intent_label + '\n')
# with open('./merge-train/label', 'w', encoding='utf-8') as f:
#     for label in merge_train_label:
#         f.write(label + '\n')
# with open('./merge-train/seq.in', 'w', encoding='utf-8') as f:
#     for seqin in merge_train_seqin:
#         f.write(seqin + '\n')
# with open('./merge-train/seq.out', 'w', encoding='utf-8') as f:
#     for seqout in merge_train_seqout:
#         f.write(seqout + '\n')
# with open('./merge-train/slot_label.txt', 'w', encoding='utf-8') as f:
#     for slot_label in merge_slot_label:
#         f.write(slot_label + '\n')
