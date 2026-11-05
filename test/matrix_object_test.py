from src import MatrixObject


def test_conversion(w: int, h: int) -> None:
    padding: int = (4 - ((w * 3) % 4)) % 4
    raw: bytes = b'\x00' * (3 * w + padding) * h
    subject: MatrixObject = MatrixObject.from_bytes(w, h, raw)
    if len(subject.data) != h:
        raise ValueError("> height is wrong")
    wrong_width: list[str] = []
    for i, row in enumerate(subject.data):
        if len(row) != w:
            wrong_width.append(str(i))
    if wrong_width:
        raise ValueError(f"> width is wrong at row(s):\n>\t{'\n>\t'.join(wrong_width)}")
    
    converted: bytes = subject.to_bytes(padding)
    if converted != raw:
        raise ValueError(f"> conversion wrong:\nexpected: {raw}\ngot:{converted}")


print("MatrixObject:")

matrix: MatrixObject = MatrixObject(1, 1)
if matrix.data != [[None]]:
    raise SystemExit("> constructor failed")

test_conversion(1, 1)
test_conversion(825, 714)

print("> ok\n")
