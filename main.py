# Индивидуальное задание к практической номер 4
# Николаева София
# группа: АДЭУ-201
# вариант 10
# Квитанция, накладная, документ, счет

class Document:
    def __init__(self, name, number, date, addressee):
        self.name = name
        self.number = number
        self.date = date
        self.addressee = addressee

    def requisites(self):
        print(f'НАЗВАНИЕ: {self.name}; НОМЕР: {self.number}; ДАТА: {self.date}; АДРЕСАНТ: {self.addressee}')

    def approved(self):
        organization = input('введите наименование органа в творительном падеже: ')
        date_of_approval = input('введите дату утверждения документа: ')
        print(f'{self.name} {self.number} от {self.date} к {self.addressee} '
              f'УТВЕРЖДЕНО {organization} {date_of_approval}')

    def agreed(self):
        agency = input('введите наименование органа в творительном падеже: ')
        date_of_agreement = input('введите дату согласования документа: ')
        print(f'СОГЛАСОВАНО {agency} {date_of_agreement}')

    def signature(self):
        d = input('Введите дату подписания: ')
        sign = input("Подпишите документ: ")
        decryption = input("Расшифруйте подпись - фамилия и инициалы: ")
        print(f"ДАТА: {d} ПОДПИСЬ: {sign} РАСШИФРОВКА ПОДПИСИ: {decryption}")


class Invoice(Document):
    def __init__(self, number, date, to_whom, from_whom, name = 'НАКЛАДНАЯ',):
        self.name = name
        self.number = number
        self.date = date
        self.to_whom = to_whom
        self.from_whom = from_whom

    def requisites(self):
        print(f'НАЗВАНИЕ: {self.name}; НОМЕР: {self.number}; ДАТА: {self.date}; КОМУ: {self.to_whom}; ОТ КОГО: {self.from_whom}')

    def info_about_good(self):
        number_of_good = input('введите номер товара: ')
        name_of_good = input('введите название товара: ')
        count_of_good = int(input('введите количество товара: '))
        cost_of_good = int(input('введите цену товара: '))
        sum_of_good = count_of_good * cost_of_good
        print(f'НОМЕР: {number_of_good}; НАЗВАНИЕ: {name_of_good}; КОЛИЧЕСТВО: {count_of_good}; ЦЕНА: {cost_of_good}; СУММА: {sum_of_good}')

    def signature(self):
        d = input('Введите дату подписания: ')
        sign_who_passed = input("Подпись того, кто сдал: : ")
        decryption_who_passed = input("Расшифрвка подписи, кто сдал: ")
        sign_who_accepted = input("Подпись того, кто принял: : ")
        decryption_who_accepted = input("Расшифрвка подписи, кто принял: ")
        print(f"ДАТА: {d} СДАЛ: {sign_who_passed} {decryption_who_passed} ПРИНЯЛ: {sign_who_accepted} {decryption_who_accepted}")


class Receipt(Document):
    def __init__(self, number, date, customer, name = 'КВИТАНЦИЯ',):
        self.name = name
        self.number = number
        self.date = date
        self.customer = customer

    def requisites(self):
        print(f'НАЗВАНИЕ: {self.name}; НОМЕР: {self.number}; ДАТА: {self.date}; ЗАКАЗЧИК: {self.customer}')

    def info_about_service(self):
        number_of_service = input('введите номер услуги/работы: ')
        name_of_service = input('введите название услуги/работы: ')
        cost_of_service = int(input('введите цену услуги/работы: '))
        print(f'НОМЕР: {number_of_service}; НАЗВАНИЕ: {name_of_service}; ЦЕНА: {cost_of_service}')

    def signature(self):
        d = input('Введите дату подписания: ')
        sign_who_payed = input("Подпись того, кто оплатил: : ")
        decryption_who_payed = input("Расшифрвка подписи, кто оплатил: ")
        sign_who_got = input("Подпись того, кто получил: : ")
        decryption_who_got = input("Расшифрвка подписи, кто получил: ")
        print(f"ДАТА: {d} ОПЛАТИЛ: {sign_who_payed} {decryption_who_payed} ПОЛУЧИЛ: {sign_who_got} {decryption_who_got}")
        print('квитанция является бланком строгой отчетности')

class Bill(Document):
    def __init__(self, number, date, name = 'СЧЕТ НА ОПЛАТУ'):
        self.name = name
        self.number = number
        self.date = date

    def requisites(self):
        print(f'НАЗВАНИЕ: {self.name}; НОМЕР: {self.number}; ДАТА: {self.date}')

    def info_about_service(self):
        number_of_service = input('введите номер услуги/работы: ')
        name_of_service = input('введите название услуги/работы: ')
        cost_of_service = int(input('введите цену услуги/работы: '))
        print(f'НОМЕР: {number_of_service}; НАЗВАНИЕ: {name_of_service}; ЦЕНА: {cost_of_service}')




doc1 = Document('Приказ', "123", '20.04.2013', 'Иванов')
print(doc1.requisites())
print(doc1.approved())
print(doc1.agreed())
print(doc1.signature())
doc2 = Invoice('123', '12.04.2019', "Иванов", 'Иванова')
print(doc2.requisites())
print(doc2.info_about_good())
print(doc2.signature())
doc3 = Receipt('123', '12.09.2012', 'Иванов')
print(doc3.requisites())
print(doc3.info_about_service())
print(doc3.signature())
doc4 = Bill('123', '16.08.2020')
print(doc4.requisites())
print(doc4.info_about_service())
print(doc4.signature())








