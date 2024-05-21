GOTO = {
    0: {
        'CODE': 1,
        'VDECL': 2,
        'FDECL': 3
    },
    2: {
        'CODE': 5,
        'VDECL': 2,
        'FDECL': 3
    },
    3: {
        'CODE': 6,
        'VDECL': 2,
        'FDECL': 3
    },
    4: {
        'ASSIGN': 8
    },
    10: {
        'ARG': 13
    },
    11: {
        'RHS': 15,
        'EXPR': 16,
        'TERM': 20,
        'FACTOR': 22
    },
    21: {
        'EXPR': 29,
        'TERM': 20,
        'FACTOR': 22
    },
    26: {
        'MOREARGS': 31
    },
    27: {
        'TERM': 33,
        'FACTOR': 22
    },
    28: {
        'FACTOR': 34
    },
    30: {
        'VDECL': 38,
        'ASSIGN': 39,
        'BLOCK': 36,
        'STMT': 37
    },
    36: {
        'RETURN': 45
    },
    37: {
        'VDECL': 38,
        'ASSIGN': 39,
        'BLOCK': 47,
        'STMT': 37
    },
    42: {
        'ASSIGN': 8
    },
    46: {
        'RHS': 54,
        'EXPR': 16,
        'TERM': 20,
        'FACTOR': 22
    },
    49: {
        'COND': 55
    },
    50: {
        'COND': 57
    },
    52: {
        'MOREARGS': 58
    },
    63: {
        'VDECL': 38,
        'ASSIGN': 39,
        'BLOCK': 66,
        'STMT': 37
    },
    65: {
        'VDECL': 38,
        'ASSIGN': 39,
        'BLOCK': 67,
        'STMT': 37
    },
    68: {
        'ELSE': 70
    },
    72: {
        'VDECL': 38,
        'ASSIGN': 39,
        'BLOCK': 73,
        'STMT': 37
    }
}

for state, transitions in GOTO.items():
    for token, next_state in transitions.items():
        print(f'GOTO[{state}][{token}] = {next_state}')
