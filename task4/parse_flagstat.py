# parse_flagstat.py

def parse_flagstat(filename="flagstat_output.txt"):
    with open(filename, "r") as f:
        lines = f.readlines()

    # Извлекаем количество ридов
    total_reads = int(lines[0].split()[0])  # Общее количество ридов
    mapped_reads = int(lines[6].split()[0])  # Картированные риды
    mapped_percentage = (mapped_reads / total_reads) * 100

    print(f"Total reads: {total_reads}")
    print(f"Mapped reads: {mapped_reads}")
    print(f"Mapped reads percentage: {mapped_percentage:.2f}%")

    # Проверка качества
    if mapped_percentage > 90:
        print("Quality Check: OK " + str(mapped_percentage))
    if mapped_percentage > 80:
        print("Quality Check: GOOD " + str(mapped_percentage))
    else:
        print("Quality Check: BAD " + str(mapped_percentage))

# Запускаем функцию, если файл исполняется как скрипт
if __name__ == "__main__":
    parse_flagstat()
