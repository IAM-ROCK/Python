name=input("Enter the name: ")

print(f"Good afternoon {name}")

letter='''Dear <|Name|>,
        You are selected!
        <|Date|>'''
        
print(letter.replace("<|Name|>","Deekshith").replace("<|Date|>","13/09/2025"))        

k="deekshith is   a good boy"
print(k.find("  "))