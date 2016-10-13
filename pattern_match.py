# Wildcard string matching

# Given a string and a pattern, write a function to check whether the string matches the pattern. The pattern can contain '.' and '*', dot means matching any one character, star means matching zero to more characters.


def pattern_match(s,p):

    if('*' not in p):
        return matchdotonly(s, p)

    isStar = (p[0] == "*")
    si = 0
    sj = 0

    for pchunk in (p.split("*")):

        # if there are multiple stars (*) continuously then just pass all except one
        if(pchunk == ''):
            isStar = True
            sj += 1
            continue

        len_s_remaining = len(s[si:])
        len_p_remaining = len(''.join(p.split("*")[sj+1:]))

        if isStar:
            matched = False
            # replace star (*) with several number (0+) of dots (.) that represent any letter
            while len_s_remaining - len_p_remaining - len(pchunk) >= 0:
                if(matchdotonly(s[si:si+len(pchunk)], pchunk)):
                    matched = True
                    break
                pchunk = '.' + pchunk

            if(not matched):
                return False

        else:

            if(not matchdotonly(s[si:si+len(pchunk)], pchunk)):
                return False

        si += len(pchunk)
        sj += 1

        isStar = True

    return True

# compare string and pattern with "." symbol by symbol
def matchdotonly(s,p):

    if(len(s) != len(p)):
        return False

    for k in range(len(s)):
        if(k >= len(p)):
            return False

        if(s[k] == p[k] or p[k] == "."):
            continue
        else:
            return False
    return True


if __name__ == '__main__':

    print "--- True tests ---"

    s = 'abcdef'
    p = 'abcdef'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a.c..f'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a*c*f'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a******f'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a**..**.**f'
    print pattern_match(s, p)

    print "--- False tests ---"

    s = 'abcdef'
    p = 'abcqdef'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a.e..f'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a*q*f'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a.....f'
    print pattern_match(s, p)

    s = 'abcdef'
    p = 'a...f'
    print pattern_match(s, p)
