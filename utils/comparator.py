def compare_documents(text1, text2):

    lines1 = set(text1.splitlines())
    lines2 = set(text2.splitlines())

    added = lines2 - lines1
    removed = lines1 - lines2

    return {
        "Added Content": list(added)[:20],
        "Removed Content": list(removed)[:20]
    }
