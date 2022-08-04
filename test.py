import numpy as np


def main():
    A = np.floor(np.random.rand(100)*10)
    print(A)
    print(np.size(A))
    print(A[1])
    # a = np.array([[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 7]],[[1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]])
    # print(type(a))
    # print(a.dtype)
    # print(a.ndim)
    # print(a.shape)
    # print(a[0,0])
    # print(a[0][0])
    # z=np.zeros(3)
    # idx=np.argwhere(a==7)
    id=np.where(A==7)
    # # print(z)
    print(*id)
    # print(idx)

if __name__ == "__main__":
    main()
