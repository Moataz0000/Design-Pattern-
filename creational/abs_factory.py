from abc import ABC, abstractmethod



# Interface
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass



# Concrete Implementations
class PaypalPayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Pay using paypal {amount}$")

class StripePayment(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Pay using stripe {amount}$")

    

# The factory
class PaymentFactory:
    @staticmethod
    def get_processor(method_name):
        processors = {
            "paypal": PaypalPayment,
            "stripe": StripePayment,
        }

        processor_method = processors.get(method_name)
        if not processor_method:
            raise ValueError(f"This {method_name} is not supported!")
        return processor_method()
    

payment_method = "x"

processor = PaymentFactory.get_processor(payment_method)
processor.process_payment(100)