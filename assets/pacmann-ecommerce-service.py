# import the library
from tabulate import tabulate

# input data/dummy data here as dict
user_data = {
    'rafie_d': 'Platinum',
    'bret_di': 'Gold',
    'tuma_tumtum': 'Platinum'
}

# input data/dummy data here as dict
harga_barang = {
    'ciki': 5000,
    'whiskas': 7500,
    'air putih': 2500,
    'mie sukses': 4500,
    'kopi susu': 18000
}


# create class Member to give the solution
class Member:
  # check the benefit:
  def check_benefit(self):
    # create the headers
    headers = ['Membership', 'Discount', 'Benefit']

    # put the data
    tables = [
             ['Platinum', '15%', 'Benefit gold + Voucher liburan + Cashback max. 30%'],
             ['Gold', '10%', 'Benefit silver + Voucher ojek online'],
             ['Silver', '8%', 'Voucher makanan']
        ]

    # return the table
    print(tabulate(tables, headers, tablefmt='github'))

  # check the membership's tier t&c (how many monthly expenses and monthly incomes are needed)
  def check_requirement(self):
    # create the headers
    headers_req = ['Tier Membership', 'Monthly Expense (Juta)', 'Monthly Income (Juta)']

    # put the data
    tables_req = [
             ['Platinum', 8, 15],
             ['Gold', 6, 10],
             ['Silver', 5, 7]
        ]

    # return the table
    print(tabulate(tables_req, headers_req, tablefmt='github'))

  # predict the users' membership through euclidean distance using monthly expenses and monthly incomes, according to the requirement's table
  def predict_membership(self, username, monthly_expense: float, monthly_income: float):
    self.username = username
    self.monthly_expense = monthly_expense
    self.monthly_income = monthly_income

    # initiate parameter data according to the requirement's table
    parameter_data = [[8,15],
                      [6,10],
                      [5,7]]

    # create empty list to store value
    result_list = []

    # iterate the membership tier
    for idx in range(len(parameter_data)):

      # create the conditional if the monthly expense lesser than monthly income, the code would work:
      if monthly_expense < monthly_income:

        # calculate the distance
        dist = round(((monthly_expense - parameter_data[idx][0])**2 + (monthly_income - parameter_data[idx][1])**2)**0.5)

        result_list.append(dist)

      # if the conditional is not met:
      else:
        raise Exception("The incomes cannot lesser than the expenses")

    # return the tier dictionary
    tier_dict = {
        'Platinum': result_list[0],
        'Gold': result_list[1],
        'Silver': result_list[2]

    }

    # return the shortest distance from result_list
    min_distance = min(result_list)

    # iterate the data from dict
    for key, value in tier_dict.items():

      # if the value is met with the shortest distance
      if value == min_distance:
        final_tier = key
        break

    # if not met
    else:
      raise Exception('There is no tier met')

    # print the result
    print(f"Hasil perhitungan Euclidean Distance dari user {self.username} adalah {tier_dict}")
    print(f"Tier membership dari user {self.username} adalah {final_tier}")

  # check total payment that user must pay with each of their membership tier
  def calculated_price(self, username, harga_barang):
    self.username = username
    self.harga_barang = harga_barang

    # acquire the tier from username
    tier = user_data[username]

    # acquire total cost before getting discounted
    total_paid = sum(harga_barang.values())

    # return the discounted price according to the tier
    if tier == 'Platinum':
      discounted_price =  total_paid - (total_paid * 0.15)
    elif tier == 'Gold':
      discounted_price =  total_paid - (total_paid * 0.10)
    elif tier == 'Silver':
      discounted_price =  total_paid - (total_paid * 0.08)
    
    # print the result
    print(f"Total yang harus dibayar oleh user {self.username} adalah {discounted_price} setelah di-diskon")


tets_obj = Member()
tets_obj.check_benefit()
print('')
tets_obj.check_requirement()
print('')
tets_obj.predict_membership('rafie_d', 100, 150)
print('')
tets_obj.calculated_price('rafie_d', harga_barang)