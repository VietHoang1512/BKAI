import os
import random

with open('./dev/label', 'r', encoding='utf-8') as f:
    dev_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev/seq.in', 'r', encoding='utf-8') as f:
    dev_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev/seq.out', 'r', encoding='utf-8') as f:
    dev_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

with open('./train/label', 'r', encoding='utf-8') as f:
    train_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./train/seq.in', 'r', encoding='utf-8') as f:
    train_seqin = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./train/seq.out', 'r', encoding='utf-8') as f:
    train_seqout = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

all_label = dev_label + train_label
all_seqin = dev_seqin + train_seqin
all_seqout = dev_seqout + train_seqout

with open('./dev/intent_label.txt', 'r', encoding='utf-8') as f:
    intent_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]
with open('./dev/slot_label.txt', 'r', encoding='utf-8') as f:
    slot_label = [line[:-1] if line.endswith('\n') else line for line in f.readlines()]

label_data_dict = dict()
for label in intent_label:
    label_data_dict[label] = [(x, y, z) for x, y, z in zip(all_label, all_seqin, all_seqout) if x == label]

for key, value in label_data_dict.items():
    print(key, len(value))

def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]

def split_folk(n_folk=5):
    if not os.path.exists('./%d-folks/' % (n_folk)):
        os.makedirs('./%d-folks/' % (n_folk))
    else:
        print("Have splited with %d folks" % (n_folk))
        return
    for folk in range(n_folk):
        if not os.path.exists('./%d-folks/folk-%d' % (n_folk, folk + 1)):
            os.makedirs('./%d-folks/folk-%d' % (n_folk, folk + 1))
        if not os.path.exists('./%d-folks/folk-%d/dev/' % (n_folk, folk + 1)):
            os.makedirs('./%d-folks/folk-%d/dev/' % (n_folk, folk + 1))
        if not os.path.exists('./%d-folks/folk-%d/train/' % (n_folk, folk + 1)):
            os.makedirs('./%d-folks/folk-%d/train/' % (n_folk, folk + 1))

    split_data_dict = dict()
    for key, value in label_data_dict.items():
        split_data_dict[key] = partition(value, n_folk)
    folk_dict = dict()
    for folk in range(n_folk):
        folk_dict[folk] = list()
        for key, value in split_data_dict.items():
            folk_dict[folk].extend(value[folk])

    for key, value in folk_dict.items():
        print(key, len(value))

    for key, value in folk_dict.items():
        dev_label = [sample[0] for sample in value]
        dev_seqin = [sample[1] for sample in value]
        dev_seqout = [sample[2] for sample in value]
        train_label = [label for label, seqin in zip(all_label, all_seqin) if seqin not in dev_seqin]
        train_seqin = [seqin for seqin in all_seqin if seqin not in dev_seqin]
        train_seqout = [seqout for seqout, seqin in zip(all_seqout, all_seqin) if seqin not in dev_seqin]
        with open('./%d-folks/folk-%d/dev/intent_label.txt' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for label in intent_label:
                f.write(label + '\n')
        with open('./%d-folks/folk-%d/dev/slot_label.txt' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for label in slot_label:
                f.write(label + '\n')
        with open('./%d-folks/folk-%d/dev/label' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for label in dev_label:
                f.write(label + '\n')
        with open('./%d-folks/folk-%d/dev/seq.in' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for seqin in dev_seqin:
                f.write(seqin + '\n')
        with open('./%d-folks/folk-%d/dev/seq.out' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for seqout in dev_seqout:
                f.write(seqout + '\n')
        with open('./%d-folks/folk-%d/train/intent_label.txt' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for label in intent_label:
                f.write(label + '\n')
        with open('./%d-folks/folk-%d/train/slot_label.txt' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for label in slot_label:
                f.write(label + '\n')
        with open('./%d-folks/folk-%d/train/label' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for label in train_label:
                f.write(label + '\n')
        with open('./%d-folks/folk-%d/train/seq.in' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for seqin in train_seqin:
                f.write(seqin + '\n')
        with open('./%d-folks/folk-%d/train/seq.out' % (n_folk, key + 1), 'w', encoding='utf-8') as f:
            for seqout in train_seqout:
                f.write(seqout + '\n')
                    
if __name__ == '__main__':
    split_folk(n_folk=5)
    split_folk(n_folk=6)