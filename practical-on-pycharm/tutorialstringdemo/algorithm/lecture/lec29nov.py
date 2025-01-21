"""students={
    "student1":{
        "name":"Shyam",
        "age":25
    },
    "student2": {
    "name": "Bob",
            "age":26
    }
}
print(students["student1"]["name"])
s1=students["student1"]
print(s1)
for key in sorted(s1):
    print(f"{key}: {s1[key]}")

locations={(19.0760,72.8777):"Mumbai",(28.7041,77.1025):"Delhi"}
print(locations[(19.0760,72.8777)])#Mumbai

numbers=[1,2,3,4,5]
squares={num:num**2 for num in numbers}#Dictionary of squares
print(squares)#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
even_squares={num:num**2 for num in numbers if num%2==0}#Dictionary of even squares
print(even_squares)#{2: 4, 4: 16}

#Merging dictionary
sales_q1={"product_a":500,"product_b":300}
sales_q2={"product_b":200,"product_c":400}
print({**sales_q1,**sales_q2})#{'product_a': 500, 'product_b': 200, 'product_c': 400}

from collections import Counter
combined_sales=dict(Counter(sales_q1)+Counter(sales_q2))
print(combined_sales)#{'product_a': 500, 'product_b': 500, 'product_c': 400}
"""
text="hello world hello python world"
words=text.split()
word_count={}
for word in words:
    word_count[word]=word_count.get(word,0)+1
print(word_count)

d={"x":1}
d[None]=2
print(d)#{"x":1,None:2}