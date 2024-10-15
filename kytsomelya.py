import string

def process_text(text):
    # 1. Перетворення тексту в нижній регістр
    lower_text = text.lower()

    # 2. Заміна ком на крапки та видалення розділових знаків
    replaced_text = lower_text.replace(',', '.')
    cleaned_text = replaced_text.translate(str.maketrans('', '', string.punctuation))

    # 3. Розбиття тексту на список слів
    words_list = cleaned_text.split()

    # 4. Додані функції
    only_alpha = cleaned_text.isalpha()  # Перевіряємо, чи всі символи - літери
    position_of_word = cleaned_text.find('замза')  # Знаходимо позицію підрядка
    right_justified_text = cleaned_text.rjust(150)  # Вирівнюємо текст праворуч


    print("Оброблений текст:", right_justified_text)
    print("Кількість слів у тексті:", len(words_list))
    print(f"Позиція слова 'Замза': {position_of_word}")
    print(f"Чи містить текст лише літери: {only_alpha}")

    return words_list, len(words_list)

# Тестовий текст
text = ("Одного разу, прокинувшись вранці після неспокійного сну, Ґреґор Замза виявив, що він перетворився "
"на величезну комаху. Лежачи на панцирно-твердій спині, він бачив перед собою, піднявши трохи голову, "
"своє опукле, коричневе, розділене на жорсткі дуги черевце, на вершині якого ковзала на межі ось-ось зісковзнути ковдра. "
"Його численні, жалюгідно тонкі ніжки, у порівнянні з рештою тіла, безпорадно дриґали перед очима.")

process_text(text)
# студент Куцомеля Денис повинен додати функції "isalpha", "find", "rjust"
# студент Гордієнко Владислав повинен додати функції "isdigit" "swapcase" "partition"
