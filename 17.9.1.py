spi = input("Введите последовательность чисел через пробел: ")
spi_list = [int(a) for a in spi.split()]

num = int(input("Введите рандомное число: "))
if num % 1 == 0:
    spi_list.append(num)
    print("Список чисел до сортировки: ", spi_list)

def sortir(spi_list):
    for i in range(len(spi_list)):
        idx_min = i
        for j in range(i, len(spi_list)):
            if spi_list[j] < spi_list[idx_min]:
                idx_min = j
        if i != idx_min:
            spi_list[i], spi_list[idx_min] = spi_list[idx_min], spi_list[i]
    return spi_list

print("Список чисел после сортировки:", sortir(spi_list))