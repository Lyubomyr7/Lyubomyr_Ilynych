def reverse(st):
    # Your Code Here
    st_s = st.split()
    st_revers = st_s[::-1]
    st_join = " ".join(st_revers)

    return st_join