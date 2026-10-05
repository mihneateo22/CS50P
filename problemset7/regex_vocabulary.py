'''
.        any char except newline      [abc]   one of a, b, c
*        0 or more                    [^abc]  anything EXCEPT a, b, c
+        1 or more                    [a-z]   a range
?        0 or 1 (optional)            \d \D   digit / non-digit
{m}      exactly m                    \w \W   word char / non-word
{m,n}    between m and n              \s \S   whitespace / non-whitespace
^  $     start / end of string        A|B     A or B
(...)    capturing group              (?:...) group that doesn't capture
'''