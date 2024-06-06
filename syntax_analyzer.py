import sys

GOTO = {
    0: {'CODE': 1, 'VDECL': 2, 'FDECL': 3},
    2: {'CODE': 5, 'VDECL': 2, 'FDECL': 3},
    3: {'CODE': 6, 'VDECL': 2, 'FDECL': 3},
    4: {'ASSIGN': 8},
    10: {'ARG': 13},
    11: {'RHS': 15, 'EXPR': 16, 'TERM': 20, 'FACTOR': 22},
    21: {'EXPR': 29, 'TERM': 20, 'FACTOR': 22},
    26: {'MOREARGS': 31},
    27: {'TERM': 33, 'FACTOR': 22},
    28: {'FACTOR': 34},
    30: {'VDECL': 38, 'ASSIGN': 39, 'BLOCK': 36, 'STMT': 37},
    36: {'RETURN': 45},
    37: {'VDECL': 38, 'ASSIGN': 39, 'BLOCK': 47, 'STMT': 37},
    42: {'ASSIGN': 8},
    46: {'RHS': 54, 'EXPR': 16, 'TERM': 20, 'FACTOR': 22},
    49: {'COND': 55},
    50: {'COND': 57},
    52: {'MOREARGS': 58},
    63: {'VDECL': 38, 'ASSIGN': 39, 'BLOCK': 66, 'STMT': 37},
    65: {'VDECL': 38, 'ASSIGN': 39, 'BLOCK': 67, 'STMT': 37},
    68: {'ELSE': 70},
    72: {'VDECL': 38, 'ASSIGN': 39, 'BLOCK': 73, 'STMT': 37}
}

ACTION = {
    0: {'vtype': ('s', 4), '$': ('r', 3)},
    1: {'$': ('a', 'cc')},
    2: {'vtype': ('s', 4), '$': ('r', 3)},
    3: {'vtype': ('s', 4), '$': ('r', 3)},
    4: {'id': ('s', 7)},
    5: {'$': ('r', 1)},
    6: {'$': ('r', 2)},
    7: {'semi': ('s', 9), 'assign': ('s', 11), 'lparen': ('s', 10)},
    8: {'semi': ('s', 12)},
    9: {'vtype': ('r', 4), 'id': ('r', 4), 'rbrace': ('r', 4), 'if': ('r', 4), 'while': ('r', 4), 'return': ('r', 4), '$': ('r', 4)},
    10: {'vtype': ('s', 14), 'rparen': ('r', 20)},
    11: {'id': ('s', 23), 'literal': ('s', 17), 'character': ('s', 18), 'boolstr': ('s', 19), 'lparen': ('s', 21), 'num': ('s', 24)},
    12: {'vtype': ('r', 5), 'id': ('r', 5), 'rbrace': ('r', 5), 'if': ('r', 5), 'while': ('r', 5), 'return': ('r', 5), '$': ('r', 5)},
    13: {'rparen': ('s', 25)},
    14: {'id': ('s', 26)},
    15: {'semi': ('r', 6)},
    16: {'semi': ('r', 7), 'addsub': ('s', 27)},
    17: {'semi': ('r', 8)},
    18: {'semi': ('r', 9)},
    19: {'semi': ('r', 10)},
    20: {'semi': ('r', 12), 'addsub': ('r', 12), 'rparen': ('r', 12), 'multdiv': ('s', 28)},
    21: {'id': ('s', 23), 'lparen': ('s', 21), 'num': ('s', 24)},
    22: {'semi': ('r', 15), 'addsub': ('r', 15), 'rparen': ('r', 15), 'multdiv': ('r', 15)},
    23: {'semi': ('r', 16), 'addsub': ('r', 16), 'rparen': ('r', 16), 'multdiv': ('r', 16)},
    24: {'semi': ('r', 17), 'addsub': ('r', 17), 'rparen': ('r', 17), 'multdiv': ('r', 17)},
    25: {'lbrace': ('s', 30)},
    26: {'rparen': ('r', 22), 'comma': ('s', 32)},
    27: {'id': ('s', 23), 'num': ('s', 24)},
    28: {'id': ('s', 23), 'num': ('s', 24)},
    29: {'addsub': ('s', 27), 'rparen': ('s', 35)},
    30: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41), 'return': ('r', 24)},
    31: {'rparen': ('r', 19)},
    32: {'vtype': ('s', 44)},
    33: {'semi': ('r', 11), 'addsub': ('r', 11), 'rparen': ('r', 11), 'multdiv': ('s', 28)},
    34: {'semi': ('r', 14), 'addsub': ('r', 14), 'rparen': ('r', 14), 'multdiv': ('r', 14)},
    35: {'semi': ('r', 13), 'addsub': ('r', 13), 'rparen': ('r', 13)},
    36: {'return': ('s', 46)},
    37: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41), 'return': ('r', 24)},
    38: {'vtype': ('r', 25), 'id': ('r', 25), 'rbrace': ('r', 25), 'if': ('r', 25), 'while': ('r', 25), 'return': ('r', 25)},
    39: {'semi': ('s', 48)},
    40: {'lparen': ('s', 49)},
    41: {'lparen': ('s', 50)},
    42: {'id': ('s', 51)},
    43: {'assign': ('s', 11)},
    44: {'id': ('s', 52)},
    45: {'rbrace': ('s', 53)},
    46: {'id': ('s', 23), 'literal': ('s', 17), 'character': ('s', 18), 'boolstr': ('s', 19), 'lparen': ('s', 21), 'num': ('s', 24)},
    47: {'rbrace': ('r', 23), 'return': ('r', 23)},
    48: {'vtype': ('r', 26), 'id': ('r', 26), 'rbrace': ('r', 26), 'if': ('r', 26), 'while': ('r', 26), 'return': ('r', 26)},
    49: {'boolstr': ('s', 56)},
    50: {'boolstr': ('s', 56)},
    51: {'semi': ('s', 9), 'assign': ('s', 11)},
    52: {'rparen': ('r', 22), 'comma': ('s', 32)},
    53: {'vtype': ('r', 18), '$': ('r', 18)},
    54: {'semi': ('s', 59)},
    55: {'rparen': ('s', 60), 'comp': ('s', 61)},
    56: {'rparen': ('r', 30), 'comp': ('r', 30)},
    57: {'rparen': ('s', 62), 'comp': ('s', 61)},
    58: {'rparen': ('r', 21)},
    59: {'rbrace': ('r', 33)},
    60: {'lbrace': ('s', 63)},
    61: {'boolstr': ('s', 64)},
    62: {'lbrace': ('s', 65)},
    63: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41), 'return': ('r', 24)},
    64: {'rparen': ('r', 29), 'comp': ('r', 29)},
    65: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41), 'return': ('r', 24)},
    66: {'rbrace': ('s', 68)},
    67: {'rbrace': ('s', 69)},
    68: {'vtype': ('r', 32), 'id': ('r', 32), 'rbrace': ('r', 32), 'if': ('r', 32), 'while': ('r', 32), 'else': ('s', 71), 'return': ('r', 32)},
    69: {'vtype': ('r', 28), 'id': ('r', 28), 'rbrace': ('r', 28), 'if': ('r', 28), 'while': ('r', 28), 'return': ('r', 28)},
    70: {'vtype': ('r', 27), 'id': ('r', 27), 'rbrace': ('r', 27), 'if': ('r', 27), 'while': ('r', 27), 'return': ('r', 27)},
    71: {'lbrace': ('s', 72)},
    72: {'vtype': ('s', 42), 'id': ('s', 43), 'rbrace': ('r', 24), 'if': ('s', 40), 'while': ('s', 41), 'return': ('r', 24)},
    73: {'rbrace': ('s', 74)},
    74: {'vtype': ('r', 31), 'id': ('r', 31), 'rbrace': ('r', 31), 'if': ('r', 31), 'while': ('r', 31), 'return': ('r', 31)},
}

reduction = [
    ('S', 1),
    ('CODE', 2), ('CODE', 2), ('CODE', 0),
    ('VDECL', 3), ('VDECL', 3),
    ('ASSIGN', 3),
    ('RHS', 1), ('RHS', 1), ('RHS', 1), ('RHS', 1),
    ('EXPR', 3), ('EXPR', 1), ('EXPR', 3),
    ('TERM', 3), ('TERM', 1),
    ('FACTOR', 1), ('FACTOR', 1),
    ('FDECL', 9),
    ('ARG', 3), ('ARG', 0),
    ('MOREARGS', 4), ('MOREARGS', 0),
    ('BLOCK', 2), ('BLOCK', 0),
    ('STMT', 1), ('STMT', 2), ('STMT', 8), ('STMT', 7),
    ('COND', 3), ('COND', 1),
    ('ELSE', 4), ('ELSE', 0),
    ('RETURN', 3)
]

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

def print_reject():
    print("\033[91m┌─────────────────────┐\033[0m") #Reject 출력
    print("\033[91m│                     │\033[0m")
    print("\033[91m│                     │\033[0m")
    print("\033[91m│      Reject!!       │\033[0m")
    print("\033[91m│                     │\033[0m")
    print("\033[91m│                     │\033[0m")
    print("\033[91m└─────────────────────┘\033[0m")

def make_child(reduction_num, children):
    parent_value = reduction[reduction_num][0] #reduction으로 부모 값 설정
    parent = Tree(parent_value)
    parent.children = children
    return parent

def get_color(level): #트리꾸미기용 함수
    colors = [
        "\033[38;5;187m",
        "\033[38;5;159m",
        "\033[38;5;151m",  
        "\033[38;5;223m",
        "\033[38;5;225m",
        "\033[38;5;158m",
    ]
    return colors[level % len(colors)]

def print_tree(node, level=0, is_last_child=True, indent=''): #트리 출력(트꾸 완료)
    color = get_color(level)
    reset = "\033[0m"

    if level == 0:
        print(color + node.value + reset)
    else:
        prefix = ('└─' if is_last_child else '├─')
        print(indent + color + prefix + node.value + reset)
    
    indent += color + ('    ' if is_last_child else '│   ') + reset
    
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last = (i == child_count - 1)
        print_tree(child, level + 1, is_last, indent)

def main():
    if len(sys.argv) != 2:
        print("python3 syntax_analyzer.py <input_file> 형식으로 입력해주세요.")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            content = file.read()
        tokens = content.split()
        tokens.append("$")
        print(tokens)
    except FileNotFoundError:
        print(f"File '{input_file}' not found.")
        sys.exit(1)

    state_stack = [0]
    token_stack = [] #토큰들 저장(트리 출력용)
    pointer = 0

    while True:
        current_state = state_stack[-1]
        current_token = tokens[pointer]
        action = ACTION.get(current_state, {}).get(current_token, None) #cur_state에서 cur_token으로 할 수 있는 ACTION 목록 가져옴

        if action is None: #action 없으면 현재 토큰으로 할 수 있는 거 없다는 뜻
            print_reject()
            print(f"[Error!] Unrecognized token '{current_token}' at position {pointer + 1}.")
            sys.exit(1)

        if action[0] == 's': #Shift 부분
            state_stack.append(action[1]) #다음 action으로 넘어가기 위해 stack에 추가
            token_stack.append(Tree(current_token)) #tree에 현재 토큰 추가
            pointer += 1
        elif action[0] == 'r': #Reduce 부분
            reduction_num = action[1]
            lhs, num_rhs = reduction[reduction_num] #reduction에서 lhs가 뭔지, rhs개수 가져오기(pop얼마나 할지 결정용)

            children = []
            for _ in range(num_rhs):
                child = token_stack.pop() #스택에서 자식 노드 pop
                children.append(child) #자식 노드 추가

            
            children = children[::-1] #리스트를 역순으로 정렬
            parent = make_child(reduction_num, children) #자식 노드들로 부모노드 생성
            token_stack.append(parent) #부모노드 stack에 추가
            for _ in range(num_rhs): #rhs 개수만큼 pop
                state_stack.pop()

            goto_state = GOTO.get(state_stack[-1], {}).get(lhs, None) #스택 맨 위에 있는 state랑 lhs로 할 수 있는 (action, state)가져오기
            if goto_state is None: #reduce할 거 없다는 뜻
                print_reject()
                print(f"[Error!] No GOTO entry for state {state_stack[-1]} and lhs {lhs}.")
                sys.exit(1)

            state_stack.append(goto_state) #stack에 다음 action, state 넣기
        elif action[0] == 'a': #Accept 부분
            root = token_stack[0] #stack제일 처음을 root로
            print_tree(root) #트리 출력
            print("\033[92m┌─────────────────────┐\033[0m") #Accept 호들갑 함 떨어주기
            print("\033[92m│                     │\033[0m")
            print("\033[92m│                     │\033[0m")
            print("\033[92m│      Accepted!!     │\033[0m")
            print("\033[92m│                     │\033[0m")
            print("\033[92m│                     │\033[0m")
            print("\033[92m└─────────────────────┘\033[0m")
            break
        else:
            print_reject()
            print(f"[Error!] Invalid action {action} for token {current_token} at state {current_state}.") #s, r, a아무것도 아닌 경우, 그냥 예외처리용
            sys.exit(1)


if __name__ == '__main__':
    main()