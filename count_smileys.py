# Given an array (arr) as an argument complete the function countSmileys that should return the total number of smiling faces.

# Rules for a smiling face:

# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.

# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces: ;( :> :} :]

# Example
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

def count_smileys(arr):
    eyes = ':;'
    nose = '-~'
    mouth = ')D'
    count = 0
    for face in arr:
        if len(face) == 2:
            if face[0] in eyes and face[1] in mouth:
                count += 1
        elif len(face) == 3:
            if face[0] in eyes and face[1] in nose and face[2] in mouth:
                count += 1
        else:
            continue
    return count #the number of valid smiley faces in array/list

def count_smileys2(arr):
    with_nose = [''.join([e, n, m]) for e in ':;' for n in '-~' for m in ')D']
    without_nose = [''.join([e, m]) for e in ':;' for m in ')D']
    smileys = with_nose + without_nose
    count = 0
    for face in arr:
        if face in smileys:
            count += 1
    return count #the number of valid smiley faces in array/list


print(count_smileys2([':)', ';(', ';}', ':-D']))
print(count_smileys([';D', ':-(', ':-)', ';~)']))
print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
