"""Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""

summ = 0
count_add = 0
count_out = 0
log = []


def nalog():
    global summ
    nalog_sum = summ * 0.1
    print("С вас сняли налог на богатство", nalog_sum)
    log.append(f"налог {nalog_sum}")
    summ -= nalog_sum


def deposit():
    global summ, count_add
    summ_add = int(input("Сумма: "))
    if summ_add % 50 == 0:
        summ += summ_add
        log.append(f"проступило {summ_add}")
        count_add += 1
        if count_add % 3 == 0:
            percent = summ * 0.03
            log.append(f"начислено 3 процента {percent}")
            summ += percent
    else:
        print("Введена некорректная сумма (не кратна 50)")


def take():
    global summ, count_out
    summ_out = int(input("Сумма: "))
    comission = summ_out * 0.015
    if comission < 30:
        comission = 30
    elif comission > 600:
        comission = 600

    if summ_out + comission > summ:
        print("Недостаточно средств")
    else:
        if summ_out % 50 == 0:
            summ -= summ_out + comission
            log.append(f"снято {summ_out}")
            log.append(f"комиссия за снятие {comission}")
            count_out += 1
            if count_out % 3 == 0:
                summ *= 1.03
        else:
            print("Введена некорректная сумма")


run = True

while run:
    if summ > 5_000_000:
        nalog()

    action = input("Действие: ")
    match action:
        case "q":  # Выход
            print("Выходим из банкомата")
            run = False

        case "a":  # Пополнить
            deposit()

        case "o":  # Снять
            take()

    print(f"Сумма: {summ}")
