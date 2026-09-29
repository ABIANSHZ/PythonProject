amt=10000
gst=amt*0.18
total=amt+gst
print("Total amount with GST:",total)
if total > 1000:
    discount=total*0.10
    total=total-discount
print("Total amount after discount:",total)