def count_substring(s1, s2):
    count = 0;
    s = (len(s1) - len(s2)) + 1

    for i in range(s):
        if s2 in s1[i:i + len(s2)]:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)