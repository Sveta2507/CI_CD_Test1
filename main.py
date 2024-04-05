import csv # для роботи з файлами

def country_sort(inputFile: str, outputFile: str) -> None:
    """
    Сортує список країн з наданого файлу та записує відсортований список у вказаний вихідний файл.

    :param inputFile: шлях до вхідного файлу зі списком країн
    :param outputFile: шлях до вихідного файлу, в який буде записано відсортований список країн
    :return: None
    """
    with open(inputFile, 'r') as file: # відкриваємо файл в режимі читання
        reader = csv.reader(file) # створюємо об'єкт, який буде зчитувати дані
        next(reader)  # пропускаємо перший рядок (підпис)
        # зчитуємо всі рядки з файлу, зберігаємо їх у список data
        data = [row for row in reader]

    # cортуємо дані за площею - другий елемент кожного рядка, reverse - від найбільшого до найменшого
    areaSort = sorted(data, key=lambda x: int(x[1]), reverse=True)

    # за населенням
    populationSort = sorted(data, key=lambda x: int(x[2]), reverse=True)

    with open(outputFile, 'w') as file: # відкриваємо файл, де буде результат, в режимі редагування
        writer = csv.writer(file) # створюємо об'єкт, який буде записувати дані у файл
        writer.writerow(['Country', 'Area', 'Population'])
        writer.writerow(['-------------------------------------------'])
        writer.writerow(['Sorted by Area'])
        writer.writerows(areaSort)
        writer.writerow(['-------------------------------------------'])
        writer.writerow(['Sorted by Population'])
        writer.writerows(populationSort)

country_sort('file.txt', 'output.txt') # передаємо відповідні параметри
