class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def add(a, b):
    return a + b

def minus(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Pembagian oleh nol tidak diizinkan"
    return a / b

def expression_tree(expression):
    if isinstance(expression, tuple):
        left, operator, right = expression
        root = Node(operator)
        root.left = expression_tree(left)
        root.right = expression_tree(right)
        return root
    else:
        return Node(expression)

def evaluate_tree(node):
    if node.value in ['+', '-', '*', '/']:
        left_result = evaluate_tree(node.left)
        right_result = evaluate_tree(node.right)
        if node.value == '+':
            return add(left_result, right_result)
        elif node.value == '-':
            return minus(left_result, right_result)
        elif node.value == '*':
            return mult(left_result, right_result)
        elif node.value == '/':
            return div(left_result, right_result)
    else:
        return node.value

# Contoh pohon ekspresi: (2+3) * (5-1)
expression = ((2, '+', 3), '*', (5, '-', 1))

expression_tree_root = expression_tree(expression)
result = evaluate_tree(expression_tree_root)

print("Hasil evaluasi pohon ekspresi:", result)
