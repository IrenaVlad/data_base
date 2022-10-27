import add_employe as ae
import user_interface as ui
import change_phone_number as cpn
import change_surname as cs
import delete_employe as de
import view_all_employe as vae
import export_in_file as eif


def user_choice():
    choice_num = ui.menu()
    if choice_num < 0 or choice_num > 7:
        print('\nНеверный ввод!\n\nВведите, пожалуйста, число от 0 до 7!\n')
        user_choice()
    elif choice_num == 0:
        ae.create_json()
    elif choice_num == 1:
        ae.add_to_json()
    elif choice_num == 2:
        cpn.change_phone_number()
    elif choice_num == 3:
        cs.change_surname()
    elif choice_num == 4:
        de.delete_employe()
    elif choice_num == 5:
        vae.view_all_employe()
    elif choice_num == 6:
        eif.export_txt()
    elif choice_num == 7:
        print('\nСпасибо за визит!\n\nДо новых встреч!')
        exit()