#point 1
print ("    *", "   * *", "  *   *", " *     *", 
"***   ***", "  *   *", "  *   *", "  *****", sep="\n")

#point 2
print(
    " " * 6 + "*",
    " " * 4 + "*" + " " * 3 + "*", 
    " " * 3 + "*" + " " * 5 + "*",
    " " * 2 + "*" + " " * 7 + "*",
    " " + "*" + " " * 9 + "*",
    "*" * 4 + " " * 5 + "*" * 4,
    " " * 3 + "*" + " " * 5 + "*",
    " " * 3 + "*" + " " * 5 + "*",
    " " * 3 + "*" + " " * 5 + "*",
    " " * 3 + "*" * 7,
    sep="\n")

#point 3
print(
    #ganti angka dua paling terakhir untuk menambah jumlah tanda panahanya.
    (" " * 6 + "*" + " " * 7) * 2,
    (" " * 4 + "*" + " " * 3 + "*" + " " * 5) * 2, 
    (" " * 3 + "*" + " " * 5 + "*" + " " * 4) * 2,
    (" " * 2 + "*" + " " * 7 + "*" + " " * 3) * 2,
    (" " + "*" + " " * 9 + "*" + " " * 2) * 2,
    ("*" * 4 + " " * 5 + "*" * 4 + " ") * 2,
    (" " * 3 + "*" + " " * 5 + "*" + " " * 4) * 2,
    (" " * 3 + "*" + " " * 5 + "*" + " " * 4) * 2,
    (" " * 3 + "*" + " " * 5 + "*" + " " * 4) * 2,
    (" " * 3 + "*" * 7 + " " * 4) * 2,
    sep="\n")
