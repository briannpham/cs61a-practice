def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def leaves(tree):
    """Return a list containing the leaf labels of tree
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return [label(tree)]
    else:
        return sum([leaves(b) for b in branches(tree)], [])

# Syntax

example = tree('FRAG', 
               [tree('NP',
                     [tree('DT', [tree('a')]),
                      tree('JJ', [tree('little')]),
                      tree('NN', [tree('bug')])]),
                tree('.', [tree('.')])])

from string import punctuation
contractions = ["n't", "'s", "'re", "'ve"]

def words(t):
    """Return the words of a tree as a string.

    >>> words(example)
    'a little bug.'
    """
    s = ''
    for w in leaves(t):
        no_space = (w in punctuation and w != '$') or w in contractions
        if not s or no_space:
            s = s + w
        else:
            s = s + ' ' + w
    return s

def replace(t, s, w):
    """Return a tree like T with all nodes labeled S replaced by word W.

    >>> words(replace(example, 'JJ', 'huge'))
    'a huge bug.'
    """
    if label(t) == s:
        return tree(s, [tree(w)])
    else:
        return tree(label(t), [replace(b, s, w) for b in branches(t)])
        
# Reading trees

examples = """
(ROOT (SQ (VP (COP is)
     (NP (NN that))
     (NP (NP (DT a) (JJ big) (NN bug))
      (CC or)
      (NP (DT a) (JJ little) (NN bug))))
     (. ?)))

(ROOT (FRAG (NP (DT a) (JJ little) (NN bug)) (. .)))

""".split('\n')

def read_trees(lines):
    """Return trees as lists of tokens from a list of lines.

    >>> for s in read_trees(examples):
    ...     print(s[:10])
    ['(', 'ROOT', '(', 'SQ', '(', 'VP', '(', 'COP', 'is', ')']
    ['(', 'ROOT', '(', 'FRAG', '(', 'NP', '(', 'DT', 'a', ')']
    """
    trees = []
    tokens = []
    for line in lines:
        if line.strip():
            spaced = line.replace('(', ' ( ').replace(')', ' ) ')
            tokens.extend(spaced.split())
            if tokens.count('(') == tokens.count(')'):
                trees.append(tokens)
                tokens = []
    return trees

def all_trees(path='CHILDESTreebank-curr/suppes.parsed'):
    return read_trees(open(path).readlines())

# Representing trees

def tree(label, branches=[]):
    if not branches:
        return [label]
    else:
        return ['(', label] + sum(branches, start=[]) + [')']
    
def label(t):
    if len(t) == 1:
        return t[0]
    else:
        assert t[0] == '(', t
        return t[1]
    
def branches(t):
    if t[0] != '(':
        return []
    current_branch = []
    all_branches = []
    opened = 1
    for token in t[2:]:
        current_branch.append(token)
        if token == '(':
            opened += 1
        elif token == ')':
            opened -= 1
        if opened == 1:
            all_branches.append(current_branch)
            current_branch = []
    assert opened == 0 and current_branch == [')'], t
    return all_branches

example = tree('ROOT', 
               [tree('FRAG', 
                     [tree('NP',
                           [tree('DT', [tree('a')]),
                            tree('JJ', [tree('little')]),
                            tree('NN', [tree('bug')])]),
                      tree('.', [tree('.')])])])

def replace_all(s, w):
    """Print the result of replace(t, s, w) for all syntax trees t."""
    for t in all_trees():
        r = replace(t, s, w)
        if t != r:
            print('Original: ', words(t).lower())
            print('Replaced: ', words(r).lower()) 
            input() # Wait for the user to press enter/return
        

# replace_all('NNS', 'bears')
# replace_all('NP', 'Oski')