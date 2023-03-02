import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('--type', type=str, choices=['annuity', 'diff'])
parser.add_argument('--payment', type=float)
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)

args = parser.parse_args()

type_ = args.type
payment = args.payment
principal = args.principal
interest = args.interest
periods = args.periods


def print_message(num_p):
    years = int(num_p / 12)
    months = num_p - years * 12
    if years < 1:
        if months > 1:
            print('It will take ' + str(months) + ' months to repay this loan!')
        if months == 1:
            print('It will take 1 month to repay this loan!')
    if years == 1:
        if months == 0:
            print('It will take 1 year to repay this loan!')
        if months == 1:
            print('It will take 1 year and 1 month to repay this loan!')
        if months > 1:
            print(f'It will take 1 year and {months} months to repay this loan!')
    if years > 1:
        if months == 0:
            print('It will take ' + str(years) + ' to repay this loan!')
        if months == 1:
            print('It will take ' + str(years) + ' and 1 month to repay this loan!')
        if months > 1:
            print('It will take ' + str(years) + ' years and ' + str(months) + ' months to repay this loan!')
    if months < 1:
        if years > 1:
            print('It will take ' + str(years) + ' years to repay this loan!')
        if years == 1:
            print('It will take 1 year to repay this loan!')


if args.type == 'diff' and args.payment is not None:
    print('Incorrect parameters')
elif args.type not in ['annuity', 'diff']:
    print('Incorrect Parameters')

args_list = [type_, payment, principal, periods, interest]
count_list = 0
for i in args_list:
    if i is None:
        count_list += 1
if count_list > 1:
    print('Incorrect Parameters')

if (args_list[1] is not None and args_list[1] < 0) or (args_list[2] is not None and args_list[2] < 0) or \
        (args_list[3] is not None and args_list[3] < 0) or (args_list[4] is not None and args_list[4] < 0.0) or \
        args_list[4] is None:
    print('Incorrect Parameters')
else:

    interest = interest / (12 * 100)

    if args.type == 'diff':
        payments = 0
        for month in range(1, periods + 1):
            D = (principal / periods) + interest * (principal - (principal * (month - 1)) / periods)
            payments += math.ceil(D)
            print("Month ", month, ": payment is ", math.ceil(D))
        print(f"Overpayment = {int(payments - principal)}")

    if args.type == 'annuity':
        if payment and periods:
            # principal = payment / ((interest * ((1 + interest)**payment)) / (((1 + interest)**payment) - 1))
            principal = math.floor(payment / ((interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1)))

            overpayment = math.floor(periods * payment - principal)
            print(f"Your loan principal is {principal}!")
            print(f"Overpayment = {overpayment}")
        elif principal and periods:
            payment = math.ceil(principal * (interest * (1 + interest) ** periods) / ((1 + interest) ** periods - 1))
            overpayment = round(periods * payment - principal)
            print(f"Your annuity is {payment}!")
            print(f"Overpayment = {round(overpayment)}")
        elif principal and payment:
            x = payment / (payment - interest * principal)
            base = 1 + interest
            periods = math.log(x, base)
            periods = math.ceil(periods)
            print_message(periods)
            overpayment = round(periods * payment - principal)
            print(f"Overpayment = {round(overpayment)}")
