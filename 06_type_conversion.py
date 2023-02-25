x=10              #int
y=20.4            #float
z="hello"         #string

print(type(x))
print(type(y))
print(type(z))

print(x+y)


# implicit type conversion
# x=x+y
# print(x,"type of x:, type(x)")


# explicit type conversion

age=input("what is your age ?")
print(age, type(int(age)))


ali_age=input("what is ali's age  ?")
print(ali_age, type(int(ali_age)))






# Barplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme (style="ticks",color_codes=True) 
titanic = sns.load_dataset ("titanic")
sns.catplot (x="sex",y="survived",hue="class",kind="bar",data=titanic)
plt.show()
