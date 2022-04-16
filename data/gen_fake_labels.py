import os


if __name__ == "__main__":
    datadir = "test"
    random_intent = "smart.home.set.percentage"
    random_slot = "O"

    with open(os.path.join(datadir, "seq.in"), "r") as f:
        sequences = []
        for line in f:
            sequences.append(line.strip())
    with open(os.path.join(datadir, "label"), "w") as f:
        f.write("\n".join(["{}".format(random_intent) for _ in sequences]))
    with open(os.path.join(datadir, "seq.out"), "w") as f:
        f.write("\n".join([" ".join(["{}".format(random_slot)
                for word in sequence.split()]) for sequence in sequences]))
    with open(os.path.join(datadir, "results.csv"), "w") as f:
        for i in range(len(sequences)):
            line = "{}, ".format(random_intent)
            line = line + " ".join(["{}".format(random_slot)
                                   for word in sequences[i].split()])
            f.write(line.strip()+"\n")
