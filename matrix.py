import numpy as np

# Function to Get Matrix Input
def get_matrix():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        print("Enter the matrix elements row by row:")
        elements = []
        for _ in range(rows):
            row = list(map(float, input().split()))
            if len(row) != cols:
                raise ValueError("Number of columns doesn't match.")
            elements.append(row)
        return np.array(elements)
    except ValueError as e:
        print("Error:", e)
        return None

def print_separator():
    print('\n' + '-'*30 + '\n')

def show_features():
    print_separator()
    print("Select an operation:")
    print("1. Addition (A + B)")
    print("2. Subtraction (A - B)")
    print("3. Element-wise Multiplication (A * B)")
    print("4. Dot Product (A @ B)")
    print("5. Transpose")
    print("6. Determinant")
    print("7. Inverse")
    print("8. Rank")
    print("9. Eigenvalues/Eigenvectors")
    print("10. Matrix Power")
    print("11. Symmetry Check")
    print("12. Exit")
    print_separator()

def matrix_addition(A, B):
    try:
        print("Addition:\n", A + B)
    except ValueError:
        print("Addition: Matrices must have the same dimensions.")

def matrix_subtraction(A, B):
    try:
        print("Subtraction:\n", A - B)
    except ValueError:
        print("Subtraction: Matrices must have the same dimensions.")

def matrix_elementwise_mult(A, B):
    try:
        print("Element-wise Multiplication:\n", A * B)
    except ValueError:
        print("Element-wise Multiplication: Matrices must have the same dimensions.")

def matrix_dot(A, B):
    try:
        print("Dot Product:\n", np.dot(A, B))
    except ValueError:
        print("Dot Product: Number of columns in A must equal the number of rows in B.")

def matrix_transpose(A, B):
    print("Transpose of A:\n", A.T)
    print("Transpose of B:\n", B.T)

def matrix_determinant(A, B):
    for name, M in [("A", A), ("B", B)]:
        if M.shape[0] == M.shape[1]:
            try:
                print(f"Determinant of {name}:", np.linalg.det(M))
            except np.linalg.LinAlgError:
                print(f"Determinant of {name}: Error.")
        else:
            print(f"Determinant of {name}: Not applicable (Matrix must be square).")

def matrix_inverse(A, B):
    for name, M in [("A", A), ("B", B)]:
        if M.shape[0] == M.shape[1]:
            try:
                print(f"Inverse of {name}:\n", np.linalg.inv(M))
            except np.linalg.LinAlgError:
                print(f"Inverse of {name}: Not invertible.")
        else:
            print(f"Inverse of {name}: Not applicable (Matrix must be square).")

def matrix_rank(A, B):
    print("Rank of A:", np.linalg.matrix_rank(A))
    print("Rank of B:", np.linalg.matrix_rank(B))

def matrix_eigens(A, B):
    for name, M in [("A", A), ("B", B)]:
        if M.shape[0] == M.shape[1]:
            vals, vecs = np.linalg.eig(M)
            print(f"Eigenvalues of {name}: {vals}")
            print(f"Eigenvectors of {name}:\n{vecs}")
        else:
            print(f"Eigenvalues/Eigenvectors of {name}: Not applicable (Matrix must be square).")

def matrix_power(A):
    if A.shape[0] == A.shape[1]:
        try:
            n = int(input("Enter an integer power to raise matrix A: "))
            print(f"A^{n}:\n", np.linalg.matrix_power(A, n))
        except Exception as e:
            print("Error:", e)
    else:
        print("Power: Matrix must be square.")

def check_symmetry(A, B):
    for name, M in [("A", A), ("B", B)]:
        if M.shape[0] == M.shape[1]:
            if np.allclose(M, M.T):
                print(f"{name} is symmetric.")
            else:
                print(f"{name} is NOT symmetric.")
        else:
            print(f"Symmetry: Not applicable (Matrix must be square).")

def main():
    print("Matrix Calculator")
    print("=================")
    print("Input Matrix A:")
    A = get_matrix()
    if A is None:
        return

    print("\nInput Matrix B:")
    B = get_matrix()
    if B is None:
        return

    while True:
        show_features()
        choice = input("Enter your choice (1-12): ").strip()
        if choice == '1':
            matrix_addition(A, B)
        elif choice == '2':
            matrix_subtraction(A, B)
        elif choice == '3':
            matrix_elementwise_mult(A, B)
        elif choice == '4':
            matrix_dot(A, B)
        elif choice == '5':
            matrix_transpose(A, B)
        elif choice == '6':
            matrix_determinant(A, B)
        elif choice == '7':
            matrix_inverse(A, B)
        elif choice == '8':
            matrix_rank(A, B)
        elif choice == '9':
            matrix_eigens(A, B)
        elif choice == '10':
            matrix_power(A)
        elif choice == '11':
            check_symmetry(A, B)
        elif choice == '12':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()