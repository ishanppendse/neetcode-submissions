class Solution:

    def encode(self, strs: List[str]) -> str:

        def compute_prefix(strs):
            prefix = (
                '(' +
                ','.join([str(len(i)) for i in strs]) +
                ')'
            )
            return prefix

        prefix = compute_prefix(strs)
        joint_strings = ''.join(strs)
        return prefix + joint_strings

    def decode(self, s: str) -> List[str]:

        def get_prefix(s):
            prefix = ''
            assert s[0] == '('
            idx = 1
            while idx < len(s):
                if s[idx] == ')':
                    break
                prefix += s[idx]
                idx += 1
            return prefix, s[idx+1:]
        
        def get_lengths(prefix):
            if len(prefix) == 0:
                return []
            lengths = prefix.split(',')
            lengths = [int(i) for i in lengths]
            return lengths

        prefix, s_actual = get_prefix(s)
        lengths = get_lengths(prefix)
        if len(lengths) == 0:
            return []
        decoded_s = []
        idx = 0
        for l in lengths:
            decoded_s.append(s_actual[idx:idx+l])
            idx += l
        return decoded_s
            
            
