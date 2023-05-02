def min_dfa(stari, alfabet, tranzitii, stare_start, stari_de_iesire):
    def partitii(P, T):
        r = []
        for p in P:
            split = {}
            for stare in p:
                key = tuple(T[stare][char] in p for char in alfabet)
                if key not in split:
                    split[key] = []
                split[key].append(stare)
            r.extend(split.values())
        return r

    P = [set(stari_de_iesire), set(stari) - set(stari_de_iesire)]
    T = {stare: {char: tranzitii[stare][char] for char in alfabet} for stare in stari}

    while True:
        new_P = partitii(P, T)
        if len(new_P) == len(P):
            break
        P = new_P

    stare_m = {stare: i for i, partition in enumerate(P) for stare in partition}
    new_stari = set(stare_m.values())
    new_tranzitii = {stare: {char: stare_m[T[stare][char]] for char in alfabet} for stare in new_stari}
    new_stare_start = stare_m[stare_start]
    new_stari_de_iesire = {stare_m[stare] for stare in stari_de_iesire}

    return new_stari, alfabet, new_tranzitii, new_stare_start, new_stari_de_iesire


def print_dfa(stari, alfabet, tranzitii, stare_start, stari_de_iesire):
    print(f"Stari: {stari}")
    print(f"Alfabet: {alfabet}")
    print(f"Tranzitii:")
    for stare in stari:
        for char in alfabet:
            print(f"q{stare}--{char}-->q{tranzitii[stare][char]}")
    print(f"stare_start: {stare_start}")
    print(f"Stari_de_iesire: {stari_de_iesire}")


# Exemplu de automat finit determinist (DFA):
stari = {0, 1, 2, 3, 4, 5}
alfabet = {'0', '1'}
tranzitii = {
    0: {'0': 1, '1': 2},
    1: {'0': 0, '1': 3},
    2: {'0': 5, '1': 4},
    3: {'0': 5, '1': 4},
    4: {'0': 4, '1': 4},
    5: {'0': 5, '1': 4},
}
stare_start = 0
stari_de_iesire = {5}

dfa = (stari, alfabet, tranzitii, stare_start, stari_de_iesire)
print("DFA initial:")
print_dfa(*dfa)

min_dfa = min_dfa(*dfa)
print("\nDFA minimal:")
print_dfa(*min_dfa)
