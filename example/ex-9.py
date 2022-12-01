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
        

