import sys

def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    m_st, m_ts = {}, {}
    for cs, ct in zip(s, t):
        if (cs in m_st and m_st[cs] != ct) or (ct in m_ts and m_ts[ct] != cs):
            return False
        m_st[cs] = ct
        m_ts[ct] = cs
    return True

def read_strings_from_stdin():
    data = sys.stdin.read().splitlines()
    # loại bỏ dòng trống ở đầu/cuối/giữa
    lines = [line.strip() for line in data if line.strip() != ""]
    if len(lines) >= 2:
        return lines[0], lines[1]
    # nếu chỉ có một dòng, có thể người dùng ghi 2 chuỗi trên 1 dòng:
    if len(lines) == 1:
        parts = lines[0].split()
        if len(parts) >= 2:
            return parts[0], parts[1]
    # nếu không có dòng (stdin rỗng), thử đọc từ input() tương tác
    # (trường hợp chạy trực tiếp)
    try:
        if not lines:
            s = input().strip()
            t = input().strip()
            return s, t
    except Exception:
        pass
    # không đủ dữ liệu
    return None, None

if __name__ == "__main__":
    s, t = read_strings_from_stdin()
    if s is None or t is None:
        sys.stderr.write("Error: Không tìm thấy 2 chuỗi. Hãy đảm bảo file input có 2 dòng (hoặc 2 chuỗi trên 1 dòng, cách nhau bằng space).\n")
        sys.exit(1)
    print(is_isomorphic(s, t))

