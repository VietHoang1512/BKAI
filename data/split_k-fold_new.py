import os
import random

with open("./dev/label", "r", encoding="utf-8") as f:
    dev_label = [line[:-1] if line.endswith("\n") else line for line in f.readlines()]
with open("./dev/seq.in", "r", encoding="utf-8") as f:
    dev_seqin = [line[:-1] if line.endswith("\n") else line for line in f.readlines()]
with open("./dev/seq.out", "r", encoding="utf-8") as f:
    dev_seqout = [line[:-1] if line.endswith("\n") else line for line in f.readlines()]

with open("./train/label", "r", encoding="utf-8") as f:
    train_label = [line[:-1] if line.endswith("\n") else line for line in f.readlines()]
with open("./train/seq.in", "r", encoding="utf-8") as f:
    train_seqin = [line[:-1] if line.endswith("\n") else line for line in f.readlines()]
with open("./train/seq.out", "r", encoding="utf-8") as f:
    train_seqout = [
        line[:-1] if line.endswith("\n") else line for line in f.readlines()
    ]

with open("./train-new/label", "r", encoding="utf-8") as f:
    train_new_label = [
        line[:-1] if line.endswith("\n") else line for line in f.readlines()
    ]
with open("./train-new/seq.in", "r", encoding="utf-8") as f:
    train_new_seqin = [
        line[:-1] if line.endswith("\n") else line for line in f.readlines()
    ]
with open("./train-new/seq.out", "r", encoding="utf-8") as f:
    train_new_seqout = [
        line[:-1] if line.endswith("\n") else line for line in f.readlines()
    ]

all_label = dev_label + train_label
all_seqin = dev_seqin + train_seqin
all_seqout = dev_seqout + train_seqout

new_label = dev_label + train_new_label
new_seqin = dev_seqin + train_new_seqin
new_seqout = dev_seqout + train_new_seqout

with open("./dev/intent_label.txt", "r", encoding="utf-8") as f:
    intent_label = [
        line[:-1] if line.endswith("\n") else line for line in f.readlines()
    ]
with open("./dev/slot_label.txt", "r", encoding="utf-8") as f:
    slot_label = [line[:-1] if line.endswith("\n") else line for line in f.readlines()]

label_data_dict = dict()
for label in intent_label:
    label_data_dict[label] = [
        (x, y, z) for x, y, z in zip(new_label, new_seqin, new_seqout) if x == label
    ]

for key, value in label_data_dict.items():
    print(key, len(value))


def partition(list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]


def split_fold(n_fold=5):
    if not os.path.exists("./%d-folds/" % (n_fold)):
        os.makedirs("./%d-folds/" % (n_fold))
    else:
        print("Have splited with %d folds" % (n_fold))
        return
    for fold in range(n_fold):
        if not os.path.exists("./%d-folds/fold-%d" % (n_fold, fold + 1)):
            os.makedirs("./%d-folds/fold-%d" % (n_fold, fold + 1))
        if not os.path.exists("./%d-folds/fold-%d/dev/" % (n_fold, fold + 1)):
            os.makedirs("./%d-folds/fold-%d/dev/" % (n_fold, fold + 1))
        if not os.path.exists("./%d-folds/fold-%d/train/" % (n_fold, fold + 1)):
            os.makedirs("./%d-folds/fold-%d/train/" % (n_fold, fold + 1))

    split_data_dict = dict()
    for key, value in label_data_dict.items():
        split_data_dict[key] = partition(value, n_fold)
    fold_dict = dict()
    for fold in range(n_fold):
        fold_dict[fold] = list()
        for key, value in split_data_dict.items():
            fold_dict[fold].extend(value[fold])

    for key, value in fold_dict.items():
        print(key, len(value))

    for key, value in fold_dict.items():
        dev_label = [sample[0] for sample in value]
        dev_seqin = [sample[1] for sample in value]
        dev_seqout = [sample[2] for sample in value]
        train_label = [
            label
            for label, seqin in zip(all_label, all_seqin)
            if seqin not in dev_seqin
        ]
        train_seqin = [seqin for seqin in all_seqin if seqin not in dev_seqin]
        train_seqout = [
            seqout
            for seqout, seqin in zip(all_seqout, all_seqin)
            if seqin not in dev_seqin
        ]
        with open(
            "./%d-folds/fold-%d/dev/intent_label.txt" % (n_fold, key + 1),
            "w",
            encoding="utf-8",
        ) as f:
            for label in intent_label:
                f.write(label + "\n")
        with open(
            "./%d-folds/fold-%d/dev/slot_label.txt" % (n_fold, key + 1),
            "w",
            encoding="utf-8",
        ) as f:
            for label in slot_label:
                f.write(label + "\n")
        with open(
            "./%d-folds/fold-%d/dev/label" % (n_fold, key + 1), "w", encoding="utf-8"
        ) as f:
            for label in dev_label:
                f.write(label + "\n")
        with open(
            "./%d-folds/fold-%d/dev/seq.in" % (n_fold, key + 1), "w", encoding="utf-8"
        ) as f:
            for seqin in dev_seqin:
                f.write(seqin + "\n")
        with open(
            "./%d-folds/fold-%d/dev/seq.out" % (n_fold, key + 1), "w", encoding="utf-8"
        ) as f:
            for seqout in dev_seqout:
                f.write(seqout + "\n")
        with open(
            "./%d-folds/fold-%d/train/intent_label.txt" % (n_fold, key + 1),
            "w",
            encoding="utf-8",
        ) as f:
            for label in intent_label:
                f.write(label + "\n")
        with open(
            "./%d-folds/fold-%d/train/slot_label.txt" % (n_fold, key + 1),
            "w",
            encoding="utf-8",
        ) as f:
            for label in slot_label:
                f.write(label + "\n")
        with open(
            "./%d-folds/fold-%d/train/label" % (n_fold, key + 1), "w", encoding="utf-8"
        ) as f:
            for label in train_label:
                f.write(label + "\n")
        with open(
            "./%d-folds/fold-%d/train/seq.in" % (n_fold, key + 1), "w", encoding="utf-8"
        ) as f:
            for seqin in train_seqin:
                f.write(seqin + "\n")
        with open(
            "./%d-folds/fold-%d/train/seq.out" % (n_fold, key + 1),
            "w",
            encoding="utf-8",
        ) as f:
            for seqout in train_seqout:
                f.write(seqout + "\n")
        os.system(
            "cp intent_label.txt ./%d-folds/fold-%d/intent_label.txt"
            % (n_fold, key + 1)
        )
        os.system(
            "cp slot_label.txt ./%d-folds/fold-%d/slot_label.txt" % (n_fold, key + 1)
        )
        os.system("cp -r test ./%d-folds/fold-%d/" % (n_fold, key + 1))


if __name__ == "__main__":
    split_fold(n_fold=6)
