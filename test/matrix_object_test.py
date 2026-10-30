from src import MatrixObject


print("MatrixObject:")

matrix: MatrixObject = MatrixObject(1, 1)
if matrix.data != [[None]]:
    raise SystemExit("")

print("ok\n")
