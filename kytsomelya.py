import string

def process_text(text):
    # 1. Використання вбудованої функції lower() для перетворення тексту в нижній регістр
    lower_text = text.lower()

    # 2. Використання функції replace() для заміни всіх ком у тексті на крапки
    replaced_text = lower_text.replace(',', '.')

    # 3. Використання функції split() для розбиття тексту на список слів
    words_list = replaced_text.split()

    # 4. Додані функції
    only_alpha = all(word.isalpha() for word in words_list)  # Перевіряємо, чи всі слова - літери
    position_of_word = lower_text.find('замза')  # Знаходимо позицію підрядка
    right_justified_text = replaced_text.rjust(150)  # Вирівнюємо текст праворуч

    print("Оброблений текст:", right_justified_text)
    print("Кількість слів у тексті:", len(words_list))
    print(f"Позиція слова 'замза': {position_of_word}")
    print(f"Чи містить текст лише літери: {only_alpha}")


text = ("Одного разу, прокинувшись вранці після неспокійного сну, Ґреґор Замза виявив, що він перетворився "
"на величезну комаху. Лежачи на панцирно-твердій спині, він бачив перед собою, піднявши трохи голову, "
"своє опукле, коричневе, розділене на жорсткі дуги черевце, на вершині якого ковзала на межі ось-ось зісковзнути ковдра. "
"Його численні, жалюгідно тонкі ніжки, у порівнянні з рештою тіла, безпорадно дриґали перед очима.")

process_text(text)
# студент Куцомеля Денис повинен додати функції "isalpha", "find", "rjust"
# студент Гордієнко Владислав повинен додати функції "isdigit" "swapcase" "partition"