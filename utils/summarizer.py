def generate_summary(text):

    paragraphs = text.split("\n")

    summary = []

    for para in paragraphs:

        para = para.strip()

        if len(para) > 50:
            summary.append(para)

        if len(summary) >= 5:
            break

    return "\n\n".join(summary)