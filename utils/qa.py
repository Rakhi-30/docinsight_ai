def answer_question(text, question):

    question_words = question.lower().split()

    matches = []

    lines = text.split("\n")

    for line in lines:

        for word in question_words:

            if word in line.lower():
                matches.append(line)
                break

    if matches:
        return "\n".join(matches[:10])

    return "No relevant information found."