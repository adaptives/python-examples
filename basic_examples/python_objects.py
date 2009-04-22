#!/usr/bin/python
# Filename : python_examples.py

class InvoiceItem:
  '''An item within the invoice'''
  def __str__(self):
    return self.text + ' ' + str(self.amt)    

  def __init__(self, **kwargs):
    self.text = ''
    self.amt = 0
    if kwargs['text'] != None:
      self.text = kwargs['text']
    if kwargs['amt'] != None:
      self.amt = kwargs['amt']

class Invoice:
  '''An invoice.'''
  def __str__(self):
    return self.number + ' ' + str(self.amt())

  def __init__(self, **kwargs):
    self.number = ''
    self.client = ''
    self.date = ''
    self.invoice_items = []
    
  def add_invoice_item(self, invoice_entry):
    self.invoice_items.append(invoice_entry)
  
  def amt(self):
    amt = 0
    for item in self.invoice_items:
      amt = amt + item.amt
    return amt
  
invoice_item = InvoiceItem(text='consulting April', amt=2000)
invoice = Invoice()
invoice.number = '20080422_01'
invoice.client = 'Sun Microsystems'
invoice.date = '22/04/2008'
invoice.add_invoice_item(invoice_item)
print invoice 
