import taimed


def find_good_plant(seq, avail_taim, score):
    seqs = []
    for o_taim in avail_taim:
        n_score = score
        if o_taim in taimed._dict[seq[-1]][0] or o_taim in taimed._dict[seq[-1]][1]:    # taim on SOBIV voi OK
            if o_taim in taimed._dict[seq[-1]][0]:  # taim sobib korvale
                n_score += 4
            if o_taim in taimed._dict[seq[-1]][1]:  # taim ok korvale
                n_score += 2
            if len(seq) > 1:
                if o_taim in taimed._dict[seq[-2]][0]:  # taim 1 taim eemal sobib
                    n_score += 3
                if o_taim in taimed._dict[seq[-2]][1]:  # taim 1 taim eemal ok
                    n_score += 1

            seqs.append([seq + [o_taim], [i for i in avail_taim if i != o_taim], n_score])

    return seqs


def main():
    taim_keys = taimed._dict.keys()
    finished_seqs = []
    for taim in taim_keys:
        # [[ seq, avail_taim, score ]]
        seqs = [[ [taim], [i for i in taim_keys if i != taim], 0 ]]   #stores multiple sequences
        # print(seqs)
        while len(seqs) > 0:
            seqs = find_good_plant(seqs[-1][0], seqs[-1][1], seqs[-1][2])
            n_seqs = []
            for seq in seqs:
                if len(seq[0]) != len(taim_keys):
                    n_seqs.append(seq)
                else:
                    finished_seqs.append(seq)
            seqs = n_seqs
    print("Sobivad taime jarjestused:")
    for seq in finished_seqs:
        print(f"Jarjestus: {seq[0]}", f"Skoor: {seq[2]}")
    pass


# kui jooksutame seda proge uksinda
if __name__ == "__main__":
    main()
