# 🧮 Matrix Calculator (Interactive Python CLI)

A feature-rich, beginner-friendly matrix calculator script for Python, operated from the command line. Perform common and advanced linear algebra tasks on two user-input matrices — all through an intuitive menu!

---

## ✨ Features

- Input any two matrices of your choice
- **Addition & Subtraction** (same shape required)
- **Element-wise Multiplication** (Hadamard product)
- **Dot Product** (`A @ B`)
- **Matrix Transpose** for each matrix
- **Determinant** (for square matrices)
- **Inverse** (for square, invertible matrices)
- **Rank** calculation for each matrix
- **Eigenvalues & Eigenvectors** (for square matrices)
- **Matrix Power** (raise `A` to any integer power, if square)
- **Symmetry Check** for each matrix
- Fully interactive CLI menu for operation selection
- Robust input validation and error handling

---

## 🚀 How to Run

1. **Install Python** (requires Python 3)
2. **Install NumPy:**
    ```
    pip install numpy
    ```
3. **Save the script as `matrix.py`.**
4. **Run in your terminal:**
    ```
    python matrix.py
    ```
5. **Follow the prompts** to enter two matrices and choose operations from the menu.

---

## 🧑‍💻 Usage Example

Matrix Calculator
Input Matrix A:
Enter the number of rows: 2
Enter the number of columns: 2
Enter the matrix elements row by row:
1 2
3 4

Input Matrix B:
Enter the number of rows: 2
Enter the number of columns: 2
Enter the matrix elements row by row:
5 6
7 8

Select an operation:

Addition (A + B)

Subtraction (A - B)

Element-wise Multiplication (A * B)

Dot Product (A @ B)

Transpose

Determinant

Inverse

Rank

Eigenvalues/Eigenvectors

Matrix Power

Symmetry Check

Exit

Enter your choice (1-12):
And so on!

---

## 🗂️ How It Works

- **Matrices** are stored as NumPy `ndarray` objects.
- **Operations** are accessed by user selection (menu-driven).
- **Errors** (e.g., shape mismatches, math errors) are caught and reported without crashing.
- All computations performed in memory; no data is saved externally.

---

## 📄 License

MIT License — free for learning, teaching, and tinkering.

---

A clean Python starter for mastering hands-on matrix operations!
