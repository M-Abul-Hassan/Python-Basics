print(2+3)
print('My_name_is_Abulhassan')
print(2+3)
print('My_name_is_Abulhassan')
print(2+3)
print('My_name_is_Abulhassan')
print(30+30)

# scatterplot
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme (style="ticks",color_codes=True)
titanic = sns.load_dataset("titanic")
print(titanic)
# g=sns.FacetGrid(titanic,row="sex",hue="alone")
# g=(g.map(plt.scatter,"age","fare").add_legend())
# plt.show()
