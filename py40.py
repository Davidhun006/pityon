def apply_method_to_list():
    # kérjük a felhasználótól a listát
    input_list = input("Kérlek, adj meg egy vesszővel elválasztott string listát: ").split(",")
    
    # kérjük a felhasználótól a metódust
    method = input("Kérlek, válassz egy metódust a következő lista közül: \n"
                   "1. upper() - az összes karakter nagybetűsre váltása\n"
                   "2. lower() - az összes karakter kisbetűsre váltása\n"
                   "3. title() - az összes szó kezdőbetűje nagybetűs lesz\n"
                   "4. capitalize() - az első szó nagybetűs lesz\n"
                   "5. swapcase() - a kis- és nagybetűk felcserélődnek\n"
                   "6. strip() - a string elejéről és végéről eltávolítja a whitespace karaktereket\n"
                   "7. replace() - cserélje le a stringben a megadott karakterláncot egy másikra\n"
                   "8. split() - szétválasztja a stringet a megadott karakterláncon, és egy lista elemeiként adja vissza\n"
                   "A választott metódus sorszáma: ")
    
    # alkalmazzuk a metódust a listaelemeken
    output_list = []
    for string in input_list:
        output_list.append(getattr(string, method)())

    # írjuk ki az eredeti és az új listát is
    print("Eredeti lista: ", input_list)
    print("Új lista: ", output_list)


apply_method_to_list()
