import pytest
import unittest
# from django.core import cache
# Create your tests here.
from mgr_payments.billGenerator import (CustomerBillGenerator,customerBillDetail,customerType,BaseFareCalculator,DiscountCalculator,PriorityFareCalculator,TaxCalculator,ICalculator) 


class TestCustomerBillGenerator(unittest.TestCase):
    def test_GetAllCustomerstoProcess(self):

        result =CustomerBillGenerator().GetAllCustomersToProcess()
        self.assertEqual(len(result), 3)

    def test_GetAllCustomerstoProcess_Should_fetch_all_the_customers_for_billgeneration_process(self):

        result =CustomerBillGenerator().GetAllCustomersToProcess()
        for customerDetail in result:
            self.assertIsNotNone(customerDetail.customerType)
            self.assertIsNotNone(customerDetail.name)
            self.assertIsNotNone(customerDetail.name)
            self.assertEqual(customerDetail.discount,0)
            self.assertEqual(customerDetail.discountPercentage,0)
            self.assertEqual(customerDetail.tax,0)
            self.assertEqual(customerDetail.total,0)
            self.assertEqual(customerDetail.totalNumberofPriorityRequests,2)
            self.assertEqual(customerDetail.totalNumberofRequests,5)
            self.assertEqual(customerDetail.PriorityRequestFare,0)

    def test_GenerateBill_wen_given_valid_customer_details_should_generate_monthlybills_for_all_Customers(self):

        customerBillGenerator =CustomerBillGenerator()
        customerBillGenerator.GenerateBill()
        for customerDetail in customerBillGenerator.customerBillDetails:
            self.assertIsNotNone(customerDetail.customerType)
            self.assertIsNotNone(customerDetail.name)
            self.assertIsNotNone(customerDetail.name)
            self.assertIsNotNone(customerDetail.discount)
            self.assertIsNotNone(customerDetail.discountPercentage)
            self.assertIsNotNone(customerDetail.tax)
            self.assertIsNotNone(customerDetail.total)
            self.assertIsNotNone(customerDetail.totalNumberofPriorityRequests)
            self.assertIsNotNone(customerDetail.totalNumberofRequests)
            self.assertIsNotNone(customerDetail.PriorityRequestFare)
        self.assertTrue(customerBillGenerator.isBillGenerationCompleted)
        # self.assertIsNotNone(cache.cache.get(customerBillGenerator.cacheKey))

    def test_GetAllCustomerstoProcess_should_return_customerBillDetailModel_with_default_billValues(self):

        result =CustomerBillGenerator().GetAllCustomersToProcess()
        for customerDetail in result:
            self.assertIsNotNone(customerDetail.customerType)
            self.assertIsNotNone(customerDetail.name)
            self.assertIsNotNone(customerDetail.name)
            self.assertEqual(customerDetail.discount,0)
            self.assertEqual(customerDetail.discountPercentage,0)
            self.assertEqual(customerDetail.tax,0)
            self.assertEqual(customerDetail.total,0)
            self.assertEqual(customerDetail.totalNumberofPriorityRequests,2)
            self.assertEqual(customerDetail.totalNumberofRequests,5)
            self.assertEqual(customerDetail.PriorityRequestFare,0)

    def test_GenerateMonthlyBill_when_given_valid_customer_detail_should_generate_monthlybill_for_given_Customer(self):
        customerBillGenerator =CustomerBillGenerator()
        customerDetailmock = customerBillDetail(customerType.Platinum,"Tom",5,5)
        customerBillGenerator.GenerateMonthlyBill(customerDetailmock)
        self.assertIsNotNone(customerDetailmock.name)
        self.assertEqual(customerDetailmock.name,"Tom")
        self.assertIsNotNone(customerDetailmock.discount)
        self.assertEqual(customerDetailmock.discount,5.0)
        self.assertIsNotNone(customerDetailmock.discountPercentage)
        self.assertEqual(customerDetailmock.discountPercentage,10.0)
        self.assertIsNotNone(customerDetailmock.total)
        self.assertEqual(customerDetailmock.total,49.5)
        self.assertIsNotNone(customerDetailmock.totalNumberofPriorityRequests)
        self.assertEqual(customerDetailmock.totalNumberofPriorityRequests,5)
        self.assertIsNotNone(customerDetailmock.totalNumberofRequests)
        self.assertEqual(customerDetailmock.totalNumberofRequests,5)
        self.assertIsNotNone(customerDetailmock.tax)
        self.assertEqual(customerDetailmock.tax,4.5)
        self.assertIsNotNone(customerDetailmock.PriorityRequestFare)
        self.assertEqual(customerDetailmock.PriorityRequestFare,0)

class TestBaseFareCalculator(unittest.TestCase):
    def test_GenerateBill_with_valid_Customer_detail_should_return_the_basrefare_for_request(self):
        customer = customerBillDetail(customerType.Regular,"Tom",5,5)
        BaseFareCalculator().GenerateBill(customer)
        self.assertIsNotNone(customer.baseFare)
        self.assertEqual(customer.baseFare,50.0)

    def test_GenerateBill_with_valid_Customer_detail_should_return_zero_as_basrefare_if_requestvalue_is_zero(self):
        customer = customerBillDetail(customerType.Regular,"Tom",0,5)
        BaseFareCalculator().GenerateBill(customer)
        self.assertIsNotNone(customer.baseFare)
        self.assertEqual(customer.baseFare,0.0)

class TestDiscountCalculator(unittest.TestCase):
    def test_GenerateBill_with_valid_Customer_detail_should_return_the_discountfare_for_request(self):
        customer = customerBillDetail(customerType.Regular,"Tom",5,5)
        customer.baseFare =50.0
        DiscountCalculator(ICalculator).GenerateBill(customer)
        self.assertIsNotNone(customer.discountPercentage)
        self.assertIsNotNone(customer.discount)
        self.assertEqual(customer.discountPercentage,10.0)
        self.assertEqual(customer.discount,5.0)

    def test_GenerateBill_with_valid_Customer_detail_should_return_zero_as_discountfare_if_requestvalue_is_zero(self):
        customer = customerBillDetail(customerType.Regular,"Tom",0,0)
        customer.baseFare =0
        DiscountCalculator(ICalculator).GenerateBill(customer)
        self.assertIsNotNone(customer.discountPercentage)
        self.assertIsNotNone(customer.discount)
        self.assertEqual(customer.discountPercentage,10.0)
        self.assertEqual(customer.discount,0.0)

class TestTaxCalculator(unittest.TestCase):
    def test_GenerateBill_with_valid_Customer_detail_should_return_the_taxfare_for_request(self):
        customer = customerBillDetail(customerType.Regular,"Tom",5,5)
        customer.baseFare =50.0
        customer.PriorityRequestFare = 25.0
        customer.discount =7.5
        TaxCalculator(ICalculator).GenerateBill(customer)
        self.assertIsNotNone(customer.tax)
        self.assertEqual(customer.tax,6.75)

    def test_GenerateBill_with_valid_Customer_detail_should_return_zero_as_tax_if_requestvalue_basevalue_priorityfare_are_zero(self):
        customer = customerBillDetail(customerType.Regular,"Tom",0,0)
        customer.baseFare =0
        customer.PriorityRequestFare =0
        customer.discount =0
        TaxCalculator(ICalculator).GenerateBill(customer)
        self.assertEqual(customer.tax,0.0)

class TestPriorityFareCalculator(unittest.TestCase):
    def test_GenerateBill_with_valid_Customer_detail_should_return_the_priorityfare_for_request(self):
        customer = customerBillDetail(customerType.Regular,"Tom",5,5)
        PriorityFareCalculator(ICalculator).GenerateBill(customer)
        self.assertIsNotNone(customer.PriorityRequestFare)
        self.assertEqual(customer.PriorityRequestFare,25)

    def test_GenerateBill_with_valid_Customer_detail_should_return_zero_as_tax_if_priorityrequest_is_zero(self):
        customer = customerBillDetail(customerType.Regular,"Tom",0,0)
        PriorityFareCalculator(ICalculator).GenerateBill(customer)
        self.assertEqual(customer.PriorityRequestFare,0.0)

class TestCustomerBillDetail(unittest.TestCase):
        def test_calculateTotal_when_given_valid_customer_detail_should_calculate_total_bill_amount(self):
            customerBill = customerBillDetail(customerType.Platinum,"Tom",5,5)
            customerBill.baseFare = 100.0
            customerBill.PriorityRequestFare=0.0
            customerBill.discountPercentage =10
            customerBill.discount =10.0
            customerBill.tax = 9.0
            customerBill.calculateTotal()
            self.assertIsNotNone(customerBill.total)
            self.assertEqual(customerBill.total,99)

if __name__ == '__main__':
    unittest.main()
