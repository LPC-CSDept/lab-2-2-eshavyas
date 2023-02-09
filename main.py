def main():
    ##################################################
    # Comlete your code here
    ##################################################
    reg_hours = 40
    reg_rate = 18.25
    o_rate = 27.78
    work_hours = int(input("How many hours did you work this week?: "))
    overtime_amount_hours = (work_hours - reg_hours)
    regular_charge = reg_hours * reg_rate
    overtime_charge = overtime_amount_hours * o_rate
    total_pay = regular_charge + overtime_charge
    print("Regular Charge: " + str(regular_charge))
    print("Overtime Charge: " + str(overtime_charge))
    print("Total wage: " + str(total_pay))
    # pass


if __name__ == '__main__':
    main()
